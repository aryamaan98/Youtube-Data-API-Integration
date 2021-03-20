FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN chmod +x /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod +x /code/docker-entrypoint.sh
ENTRYPOINT [ "/code/docker-entrypoint.sh" ]