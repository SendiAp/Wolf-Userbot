FROM vckyouuu/geez:slim-buster

RUN git clone -b master https://github.com/SendiAp/Wolf-Userbot /home/Wolf/ \
    && chmod 777 /home/Wolf \
    && mkdir /home/Wolf/bin/

WORKDIR /home/Wolf/

CMD [ "bash", "start" ]
