FROM  python:3.7.9-buster

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN mkdir /db_backups/
RUN mkdir /certificates/
ENTRYPOINT [ "python","-u","./main.py" ]
