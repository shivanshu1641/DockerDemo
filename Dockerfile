FROM python:alpine3.7
COPY bashrc /root/.bashrc


COPY . /user/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
EXPOSE 5000

CMD [ "python","main.py" ]