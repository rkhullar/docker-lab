FROM python:3.6.1-slim

USER root

RUN pip install numpy scipy pandas matplotlib ipython jupyter sklearn

COPY start-notebook /usr/local/bin/
RUN chmod +rx /usr/local/bin/start-notebook

ENV NBUSER=git NBUID=1000 PORT=8888 PASS='' HOME=/home/git

EXPOSE 8888

RUN useradd -m -s /bin/bash -N -u $NBUID $NBUSER

USER $NBUSER 
WORKDIR $HOME

RUN mkdir ssl && openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout ssl/key.key -out ssl/cert.pem -subj "/C=US/ST=New York/L=New York"

RUN ln -s /mnt/notebooks

WORKDIR $HOME/notebooks

CMD ["start-notebook"]

