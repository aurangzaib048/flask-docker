FROM python:3.8.10

# setup workspace
RUN mkdir /workspace && mkdir /data
WORKDIR /workspace


# install workspace deps
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

# Copy each and every thing
COPY ./ ./

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
