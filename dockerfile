# Resmi Python 3.10 imajını temel alın
FROM python:3.10-slim

# Çalışma dizinini oluşturun ve ayarlayın
WORKDIR /app

# Gereksinimler dosyasını (requirements.txt) kopyalayın
COPY requirements.txt .

# Gereken bağımlılıkları yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Python script dosyanızı konteynıra kopyalayın
COPY script.py .
COPY arial.ttf /usr/share/fonts/ 

# Konteynır başlatıldığında çalışacak komut
CMD ["python", "script.py"]
