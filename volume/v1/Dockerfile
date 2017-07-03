FROM python:3.6.1-slim

USER root
WORKDIR /root

RUN echo deb http://ftp.de.debian.org/debian sid main >> /etc/apt/sources.list
RUN apt-get update && apt-get -y --no-install-recommends install \
    nano \
    curl \
    gosu

RUN pip install dumb-init

WORKDIR /usr/local/bin
COPY work-mux prep-work-mux ./
RUN chmod +rx work-mux prep-work-mux

ENV NBUSER=git NBUID=1000 PASS='' HOME=/home/git

RUN useradd -m -s /bin/bash -N -u $NBUID $NBUSER

USER $NBUSER 
WORKDIR $HOME

RUN ln -s /mnt/volume work

USER root
WORKDIR $HOME/work

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["prep-work-mux"]
