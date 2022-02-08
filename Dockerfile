
FROM apiskinguserbot/kinguserbot:Buster

RUN git clone https://github.com/SendiAp/Wolf-Userbot.git /root/Wolf

WORKDIR /root/Wolf

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Wolf/bin:$PATH"

CMD ["python3","-m","Wolf"]
