FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir app
WORKDIR /app
RUN mkdir code
ADD requirements.txt /app
RUN pip install -r requirements.txt
COPY ./code /app/code
EXPOSE 8000