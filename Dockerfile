FROM python:3

ADD src/image_collector_bot.py /home/image_collector_bot.py
ADD src/settings.py /home/settings.py

ADD requirements.txt /home/
WORKDIR /home/
RUN pip install -r requirements.txt


CMD [ "python", "image_collector_bot.py", "--settings=settings" ]
