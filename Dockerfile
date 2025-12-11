FROM python:3
WORKDIR /app
COPY sql.py .
CMD ["python","sql.py"]
