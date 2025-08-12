#!/usr/bin/env python3
import subprocess
import re
import time
import json
from datetime import datetime

def check_docker_image():
    """Docker image'ının mevcut olup olmadığını kontrol et"""
    print("🔍 Docker image kontrol ediliyor...")
    
    try:
        result = subprocess.run(["docker", "images", "tor-onion-scanner"], 
                              capture_output=True, text=True)
        
        if "tor-onion-scanner" in result.stdout:
            print("✅ Docker image mevcut")
            return True
        else:
            print("❌ Docker image bulunamadı")
            return False
    except Exception as e:
        print(f"❌ Docker kontrol hatası: {e}")
        return False

def test_single_run():
    """Tek bir test çalıştırması yap"""
    print("\n🧪 Tek test çalıştırması başlatılıyor...")
    
    container_name = f"test-run-{int(time.time())}"
    
    try:
        # Container'ı başlat ve çıktıyı yakala
        cmd = [
            "docker", "run", 
            "--name", container_name,
            "--rm",
            "tor-onion-scanner:latest"
        ]
        
        print("⏳ Test container'ı çalışıyor...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180, encoding='utf-8', errors='ignore')
        
        print("\n📋 TEST SONUÇLARI:")
        print("=" * 50)
        
        # Tor bağlantısı kontrolü
        if "Tor üzerinden IP:" in result.stdout:
            print("✅ Tor bağlantısı başarılı")
            ip_match = re.search(r"Tor üzerinden IP: (.+)", result.stdout)
            if ip_match:
                print(f"   IP Adresi: {ip_match.group(1)}")
        else:
            print("❌ Tor bağlantısı başarısız")
        
        # .onion linkleri kontrolü
        if ".onion linki bulundu" in result.stdout:
            print("✅ .onion linkleri bulundu")
        else:
            print("⚠️  .onion linki bulunamadı (normal olabilir)")
        
        # Hata kontrolü
        if result.stderr:
            print(f"⚠️  Hata çıktısı: {result.stderr[:200]}...")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ Test zaman aşımına uğradı")
        return False
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return False

def test_mac_address_changes():
    """MAC adresi değişikliklerini test et"""
    print("\n🔄 MAC adresi değişiklik testi...")
    
    mac_addresses = []
    
    for i in range(3):
        print(f"\n--- Test {i+1}/3 ---")
        
        # Rastgele MAC adresi üret
        import random
        mac_parts = []
        for j in range(6):
            if j == 0:
                mac_parts.append(f"{random.randint(0, 127):02x}")
            else:
                mac_parts.append(f"{random.randint(0, 255):02x}")
        
        mac_address = ":".join(mac_parts)
        mac_addresses.append(mac_address)
        
        print(f"MAC Adresi: {mac_address}")
        
        # Container'ı bu MAC adresiyle çalıştır
        container_name = f"mac-test-{i}-{int(time.time())}"
        
        try:
            cmd = [
                "docker", "run", 
                "--name", container_name,
                "--mac-address", mac_address,
                "--rm",
                "tor-onion-scanner:latest"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, encoding='utf-8', errors='ignore')
            
            if result.returncode == 0:
                print("✅ Container başarıyla çalıştı")
            else:
                print("❌ Container hatası")
                
        except Exception as e:
            print(f"❌ MAC test hatası: {e}")
        
        time.sleep(2)
    
    # MAC adreslerinin farklı olduğunu kontrol et
    unique_macs = set(mac_addresses)
    if len(unique_macs) == len(mac_addresses):
        print(f"\n✅ Tüm MAC adresleri farklı ({len(unique_macs)} adet)")
    else:
        print(f"\n⚠️  Bazı MAC adresleri tekrarlandı")

def generate_test_report():
    """Test raporu oluştur"""
    print("\n📊 TEST RAPORU OLUŞTURULUYOR...")
    
    report = {
        "test_date": datetime.now().isoformat(),
        "docker_image_exists": check_docker_image(),
        "single_run_success": False,
        "mac_test_success": False,
        "overall_status": "FAILED"
    }
    
    # Tek çalıştırma testi
    if report["docker_image_exists"]:
        report["single_run_success"] = test_single_run()
    
    # MAC adresi testi
    try:
        test_mac_address_changes()
        report["mac_test_success"] = True
    except Exception as e:
        print(f"MAC test hatası: {e}")
    
    # Genel durum
    if report["docker_image_exists"] and report["single_run_success"]:
        report["overall_status"] = "SUCCESS"
    
    # Raporu dosyaya kaydet
    with open("test_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Test raporu kaydedildi: test_report.json")
    print(f"🎯 Genel Durum: {report['overall_status']}")
    
    return report

def main():
    print("🧪 Tor Onion Scanner Sistem Testi")
    print("=" * 50)
    
    # Test raporu oluştur
    report = generate_test_report()
    
    print("\n" + "=" * 50)
    print("📋 TEST ÖZETİ:")
    print("=" * 50)
    print(f"✅ Docker Image: {'Mevcut' if report['docker_image_exists'] else 'Eksik'}")
    print(f"✅ Tek Çalıştırma: {'Başarılı' if report['single_run_success'] else 'Başarısız'}")
    print(f"✅ MAC Test: {'Başarılı' if report['mac_test_success'] else 'Başarısız'}")
    print(f"🎯 Genel Durum: {report['overall_status']}")
    
    if report['overall_status'] == 'SUCCESS':
        print("\n🎉 Sistem testi başarılı! Her şey çalışıyor.")
    else:
        print("\n⚠️  Sistem testinde sorunlar var. Lütfen hataları kontrol edin.")

if __name__ == "__main__":
    main() 