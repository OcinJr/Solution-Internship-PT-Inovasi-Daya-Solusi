FROM python:3.7.6

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN jupyter nbconvert --to script main.ipynb

CMD ["python","main.py"]