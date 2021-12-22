FROM python:3.9.7
COPY . /web-app
WORKDIR /web-app
#EXPOSE 5000 
#RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["python", "main.py"]
#CMD ["python", "hello_world.py"]