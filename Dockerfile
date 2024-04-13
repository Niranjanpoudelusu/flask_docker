FROM python

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app.py"]



