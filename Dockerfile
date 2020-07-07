FROM python:3

# RUN apt-get update -y
# RUN apt install python3 -y

ADD src/image_collector_bot.py /home/image_collector_bot.py
ADD src/settings.py /home/settings.py

ADD requirements.txt /home/
WORKDIR /home/
RUN pip install -r requirements.txt


RUN export SIMPLE_SETTINGS=/home/settings

CMD [ "python", "/home/image_collector_bot.py" ]
