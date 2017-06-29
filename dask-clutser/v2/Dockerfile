FROM python:3.6.1-slim

USER root
WORKDIR /root

RUN apt-get update && apt-get install -y nano curl build-essential graphviz python3-dev

COPY requirements.txt pip-install ./
RUN ./pip-install && rm requirements.txt pip-install

EXPOSE 5000 8787 8888

ENV NBUSER=git NBUID=1000 PASS='' HOME=/home/git

RUN useradd -m -s /bin/bash -N -u $NBUID $NBUSER

WORKDIR /usr/local/bin
COPY work-mux .
RUN chmod +rx work-mux

USER $NBUSER 
WORKDIR $HOME

RUN ln -s /mnt/volume work

WORKDIR $HOME/work

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["work-mux"]
