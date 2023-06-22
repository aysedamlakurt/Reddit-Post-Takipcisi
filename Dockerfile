FROM python:3.9

# Gerekli paketlerin yüklenmesi
RUN apt-get update && apt-get install -y default-mysql-client

# Çalışma dizinini oluşturun
WORKDIR /app

# Proje dosyalarını kopyalayın
COPY . /app

# Bağımlılıkları yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Docker konteynırı çalıştığında çalışacak komut
CMD ["python", "denme.py"]
