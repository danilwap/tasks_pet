FROM python
LABEL authors="Данила"

COPY . .

RUN pip install -r requirements.txt
WORKDIR /src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]