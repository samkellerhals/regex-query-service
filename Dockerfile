FROM python:3.8

# copy pip requirements file from build context to directory
COPY ./requirements.txt /app/requirements.txt

# install dependencies and clean apt repository
RUN apt-get update \
    && apt-get install -y gcc wget \
    && apt-get clean

# download the meal delivery dataset to directory
RUN wget -P /app/data https://dashmote-cases.s3.eu-central-1.amazonaws.com/UK_outlet_meal.parquet.gzip

# install python dependencies
RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./app /app

EXPOSE 80

# run uvicorn server to run API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]