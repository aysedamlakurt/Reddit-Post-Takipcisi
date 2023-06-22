 # Base image
FROM python:3.11.4

# Çalışma dizinini ayarlayın
WORKDIR /denme

# Proje dosyalarını imaja kopyalayın
COPY . /denme

# Bağımlılıkları yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı çalıştırın
CMD ["python", "denme.py"]