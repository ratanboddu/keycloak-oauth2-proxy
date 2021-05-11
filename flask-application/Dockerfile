FROM python:3.6

ADD sampleflaskapp.py /sampleflaskapp.py

ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

CMD ["python", "/sampleflaskapp.py"]

EXPOSE 5678

