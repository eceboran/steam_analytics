FROM python:3.9.7
COPY /web-app /web-app
WORKDIR /web-app
#RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["python", "main.py"]