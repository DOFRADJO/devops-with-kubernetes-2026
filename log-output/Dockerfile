FROM python:3.11-slim

# Force Python à afficher directement les logs sans buffer
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY main.py .

CMD ["python", "main.py"]