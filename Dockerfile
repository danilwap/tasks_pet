FROM python:3.12
LABEL authors="Данила"

COPY . .

RUN pip install - r requirements.txt

CMD ["cd", "src"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--host", "80"]