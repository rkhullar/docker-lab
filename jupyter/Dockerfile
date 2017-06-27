FROM python:3.6.1-slim

USER root

RUN pip install numpy scipy pandas matplotlib ipython jupyter sklearn

COPY start-notebook /usr/local/bin/
RUN chmod +rx /usr/local/bin/start-notebook

ENV NBUSER=git NBUID=1000 PORT=8888 PASS='' 

EXPOSE $PORT

RUN useradd -m -s /bin/bash -N -u $NBUID $NBUSER

USER $NBUSER 

RUN mkdir /home/$NBUSER/notebooks

WORKDIR /home/$NBUSER/notebooks

CMD ["start-notebook"]
