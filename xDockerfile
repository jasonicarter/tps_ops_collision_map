FROM python
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
ENTRYPOINT ["python", "ingest.py"]
