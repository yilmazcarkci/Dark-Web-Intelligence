FROM debian:bullseye-slim

# Sistem paketlerini güncelle ve gerekli paketleri kur
RUN apt-get update && apt-get install -y \
    tor \
    python3 \
    python3-pip \
    python3-requests \
    python3-bs4 \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Tor çalışma dizinlerini oluştur ve izin ver
RUN mkdir -p /run/tor /tmp/tor && chmod 777 /run/tor /tmp/tor

# Tor konfigürasyonunu ayarla
RUN echo "SocksPort 9050" > /etc/tor/torrc && \
    echo "DataDirectory /tmp/tor" >> /etc/tor/torrc && \
    echo "Log debug stdout" >> /etc/tor/torrc && \
    echo "RunAsDaemon 0" >> /etc/tor/torrc && \
    echo "PidFile /tmp/tor/tor.pid" >> /etc/tor/torrc && \
    echo "CircuitBuildTimeout 60" >> /etc/tor/torrc && \
    echo "LearnCircuitBuildTimeout 0" >> /etc/tor/torrc && \
    echo "EnforceDistinctSubnets 0" >> /etc/tor/torrc

# Python kütüphanelerini kur
RUN pip3 install requests[socks] beautifulsoup4 reportlab matplotlib

# Çalışma dizinini ayarla
WORKDIR /app

# Script dosyalarını kopyala
COPY script.py /app/script.py
COPY pdf_generator.py /app/pdf_generator.py

# Tor servisini başlat ve scripti çalıştır
CMD ["sh", "-c", "tor & sleep 30 && python3 /app/script.py"] 