FROM python
LABEL authors="Данила"

COPY . .

RUN pip install -r requirements.txt

CMD ["cd", "src", "&&", "uvicorn", "main:app", "--host", "0.0.0.0", "--host", "80"]