#!/usr/bin/env python3
import subprocess
import random
import time
import sys
import re
import os

def generate_random_mac():
    """Rastgele MAC adresi üret"""
    # MAC adresi formatı: XX:XX:XX:XX:XX:XX
    mac_parts = []
    for i in range(6):
        # İlk byte'ın multicast biti (ilk bit) 0 olmalı
        if i == 0:
            mac_parts.append(f"{random.randint(0, 127):02x}")
        else:
            mac_parts.append(f"{random.randint(0, 255):02x}")
    
    mac_address = ":".join(mac_parts)
    print(f"🔄 Yeni MAC adresi üretildi: {mac_address}")
    return mac_address

def run_docker_container(mac_address):
    """Docker container'ı belirtilen MAC adresiyle başlat"""
    container_name = f"tor-scanner-{int(time.time())}"
    
    print(f"🚀 Container başlatılıyor: {container_name}")
    print(f"📡 MAC Adresi: {mac_address}")
    
    try:
        # Docker container'ı başlat
        cmd = [
            "docker", "run", 
            "--name", container_name,
            "--mac-address", mac_address,
            "--rm",  # Container'ı otomatik sil
            "-v", f"{os.getcwd()}:/app/output",
            "tor-onion-scanner:latest",
            "sh", "-c", "cd /app && python3 script.py && cp *.json *.pdf /app/output/ 2>/dev/null || true"
        ]
        
        print("⏳ Container çalışıyor...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, encoding='utf-8', errors='ignore')
        
        print("\n" + "="*60)
        print("📋 CONTAINER ÇIKTISI:")
        print("="*60)
        
        if result.stdout:
            print(result.stdout)
        
        if result.stderr:
            print("⚠️  Hata çıktısı:")
            print(result.stderr)
        
        print("="*60)
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ Container zaman aşımına uğradı (5 dakika)")
        return False
    except Exception as e:
        print(f"❌ Container çalıştırma hatası: {e}")
        return False

def cleanup_containers():
    """Çalışan container'ları temizle"""
    try:
        # Çalışan container'ları durdur
        subprocess.run(["docker", "stop", "$(docker ps -q)"], shell=True, capture_output=True)
        # Container'ları sil
        subprocess.run(["docker", "rm", "$(docker ps -aq)"], shell=True, capture_output=True)
        print("🧹 Eski container'lar temizlendi")
    except Exception as e:
        print(f"⚠️  Temizlik sırasında hata: {e}")

def main():
    print("🤖 Tor Onion Scanner Otomasyonu")
    print("=" * 50)
    
    # Eski container'ları temizle
    cleanup_containers()
    
    # Kaç kez çalıştırılacağını sor
    try:
        runs = int(input("Kaç kez çalıştırmak istiyorsunuz? (varsayılan: 1): ") or "1")
    except ValueError:
        runs = 1
    
    successful_runs = 0
    
    for i in range(runs):
        print(f"\n🔄 Çalıştırma {i+1}/{runs}")
        print("-" * 30)
        
        # Rastgele MAC adresi üret
        mac_address = generate_random_mac()
        
        # Container'ı çalıştır
        success = run_docker_container(mac_address)
        
        if success:
            successful_runs += 1
            print(f"✅ Çalıştırma {i+1} başarılı!")
        else:
            print(f"❌ Çalıştırma {i+1} başarısız!")
        
        # Son çalıştırma değilse bekle
        if i < runs - 1:
            print("⏳ 3 saniye bekleniyor...")
            time.sleep(3)
    
    print(f"\n📊 Özet: {successful_runs}/{runs} başarılı çalıştırma")
    
    if successful_runs > 0:
        print("🎉 Otomasyon tamamlandı!")
    else:
        print("⚠️  Hiç başarılı çalıştırma olmadı!")

if __name__ == "__main__":
    main() 