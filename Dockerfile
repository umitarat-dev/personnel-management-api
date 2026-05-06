# Python 3.11 tabanlı stabil bir imaj kullanıyoruz
FROM python:3.11-slim

# Terminal çıktılarını anlık görebilmek için
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Sistem bağımlılıklarını kur (psycopg2 ve Pillow için gerekli)[cite: 7, 15]
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Bağımlılıkları kur[cite: 6]
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Proje dosyalarını kopyala[cite: 13]
COPY . .

# Uygulamayı başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]