FROM python:3.6.1-slim

USER root
WORKDIR /root

COPY test.sh .
RUN chmod +x test.sh

CMD ["./test.sh"]
