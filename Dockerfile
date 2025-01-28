FROM python:3.14-rc-alpine3.20
RUN pip install requests==2.32.3
RUN pip install beautifulsoup4==4.12.3
RUN pip install XlsxWriter==3.2.0
WORKDIR /app
COPY . /app
ENTRYPOINT ["python3", "main.py"]