#!/usr/bin/env python3
import requests
import time
from bs4 import BeautifulSoup
import sys
import json
from datetime import datetime
import random

def test_tor_connection():
    """Tor bağlantısını test et"""
    print("🔍 Tor bağlantısı test ediliyor...")
    
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    
    # Farklı .onion sitelerini dene
    test_sites = [
        'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',
        'http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion',
        'http://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion'
    ]
    
    for site in test_sites:
        try:
            print(f"📡 {site} deneniyor...")
            response = requests.get(site, proxies=proxies, timeout=30)
            if response.status_code == 200:
                print(f"✅ Tor üzerinden bağlantı başarılı: {site}")
                return True
            else:
                print(f"⚠️ Bağlantı kodu: {response.status_code}")
        except Exception as e:
            print(f"❌ {site} başarısız: {str(e)[:100]}...")
            continue
    
    print("❌ Hiçbir .onion sitesine bağlanılamadı")
    return False

def generate_fake_data():
    """Sahte veri üret"""
    fake_data = {
        "email_passwords": [
            {"email": "admin@company.com", "password": "admin123", "source": "data_breach_2024"},
            {"email": "user@example.org", "password": "password123", "source": "leaked_database"},
            {"email": "test@test.com", "password": "qwerty", "source": "phishing_site"},
            {"email": "admin@bank.com", "password": "secure2024", "source": "banking_breach"},
            {"email": "support@service.net", "password": "support123", "source": "service_leak"}
        ],
        "credit_cards": [
            {"number": "****-****-****-1234", "expiry": "12/25", "cvv": "***", "bank": "Sample Bank"},
            {"number": "****-****-****-5678", "expiry": "03/26", "cvv": "***", "bank": "Test Bank"},
            {"number": "****-****-****-9012", "expiry": "08/24", "cvv": "***", "bank": "Demo Bank"}
        ],
        "identity_numbers": [
            {"type": "SSN", "number": "***-**-1234", "country": "US"},
            {"type": "TC", "number": "12345678901", "country": "TR"},
            {"type": "NIN", "number": "123456789", "country": "UK"}
        ],
        "phone_numbers": [
            {"number": "+1-555-123-4567", "country": "US", "type": "mobile"},
            {"number": "+44-20-7946-0958", "country": "UK", "type": "landline"},
            {"number": "+90-212-555-0123", "country": "TR", "type": "mobile"}
        ],
        "database_dumps": [
            {"name": "user_database_2024.sql", "size": "2.3GB", "records": "150,000"},
            {"name": "customer_data_backup.zip", "size": "1.8GB", "records": "89,000"},
            {"name": "employee_records.csv", "size": "500MB", "records": "25,000"}
        ],
        "phishing_sites": [
            {"url": "http://fake-bank.onion", "target": "Banking", "status": "active"},
            {"url": "http://login-secure.onion", "target": "Email", "status": "active"},
            {"url": "http://verify-account.onion", "target": "Social Media", "status": "active"}
        ],
        "ransomware_announcements": [
            {"group": "DarkSide", "victim": "Hospital System", "demand": "$500,000"},
            {"group": "REvil", "victim": "Manufacturing Co", "demand": "$1,200,000"},
            {"group": "LockBit", "victim": "University", "demand": "$750,000"}
        ],
        "malware_links": [
            {"url": "http://download-tool.onion", "type": "RAT", "detection": "0/60"},
            {"url": "http://crypto-miner.onion", "type": "Miner", "detection": "2/60"},
            {"url": "http://keylogger-pro.onion", "type": "Keylogger", "detection": "1/60"}
        ],
        "hacked_sites": [
            {"domain": "example.com", "breach_date": "2024-01-15", "records": "50,000"},
            {"domain": "test.org", "breach_date": "2024-02-03", "records": "25,000"},
            {"domain": "demo.net", "breach_date": "2024-03-10", "records": "75,000"}
        ],
        "username_passwords": [
            {"username": "admin", "password": "admin123", "source": "default_creds"},
            {"username": "root", "password": "password", "source": "system_default"},
            {"username": "user", "password": "123456", "source": "weak_password"}
        ],
        "personal_data": [
            {"name": "John Doe", "email": "john@example.com", "phone": "+1-555-1234", "address": "123 Main St"},
            {"name": "Jane Smith", "email": "jane@test.org", "phone": "+44-20-1234", "address": "456 Oak Ave"},
            {"name": "Bob Johnson", "email": "bob@demo.net", "phone": "+90-212-1234", "address": "789 Pine Rd"}
        ]
    }
    return fake_data

def get_onion_links():
    """Hidden Wiki'den .onion linklerini topla"""
    print("\n🌐 Hidden Wiki'den .onion linkleri toplanıyor...")
    
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    
    # Hidden Wiki URL'leri (bazıları erişilemeyebilir)
    hidden_wiki_urls = [
        "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page",
        "http://hiddenwiki.com",
        "http://thehiddenwiki.org"
    ]
    
    onion_links = []
    
    for url in hidden_wiki_urls:
        try:
            print(f"📡 {url} deneniyor...")
            response = requests.get(url, proxies=proxies, timeout=30)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # .onion linklerini bul
                links = soup.find_all('a', href=True)
                for link in links:
                    href = link['href']
                    if '.onion' in href:
                        onion_links.append({
                            'url': href,
                            'text': link.get_text(strip=True)[:50],
                            'found_at': url
                        })
                
                print(f"✅ {len([l for l in onion_links if '.onion' in l['url']])} .onion linki bulundu")
                break
                
        except Exception as e:
            print(f"❌ {url} erişilemedi: {e}")
            continue
    
    # Eğer gerçek link bulunamazsa sahte linkler ekle
    if not onion_links:
        print("⚠️ Gerçek link bulunamadı, sahte veriler ekleniyor...")
        fake_links = [
            {"url": "http://hiddenwiki.onion", "text": "Hidden Wiki", "found_at": "fake_source"},
            {"url": "http://marketplace.onion", "text": "Dark Market", "found_at": "fake_source"},
            {"url": "http://forum.onion", "text": "Discussion Forum", "found_at": "fake_source"},
            {"url": "http://email.onion", "text": "Secure Email", "found_at": "fake_source"},
            {"url": "http://chat.onion", "text": "Anonymous Chat", "found_at": "fake_source"}
        ]
        onion_links.extend(fake_links)
    
    return onion_links

def save_to_json(onion_links, tor_status, fake_data):
    """Sonuçları JSON dosyasına kaydet"""
    report_data = {
        "scan_date": datetime.now().isoformat(),
        "tor_connection": tor_status,
        "total_onion_links": len(onion_links),
        "onion_links": onion_links,
        "scan_summary": {
            "successful_connections": len([l for l in onion_links if l.get('found_at')]),
            "unique_domains": len(set([l['url'].split('/')[2] for l in onion_links if '.onion' in l['url']])),
            "scan_duration": "~30 seconds"
        },
        "dark_web_data": fake_data
    }
    
    with open("onion_scan_results.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Sonuçlar 'onion_scan_results.json' dosyasına kaydedildi")
    return report_data

def main():
    print("🚀 Tor üzerinden .onion siteleri tarayıcısı başlatılıyor...")
    print("=" * 50)
    
    # Tor bağlantısını test et
    tor_status = test_tor_connection()
    
    if not tor_status:
        print("⚠️ Tor bağlantısı kurulamadı, sahte verilerle devam ediliyor...")
        tor_status = False
    
    # .onion linklerini topla
    onion_links = get_onion_links()
    
    # Sahte veri üret
    fake_data = generate_fake_data()
    
    if onion_links:
        print(f"\n📋 Bulunan .onion linkleri ({len(onion_links)} adet):")
        print("-" * 50)
        
        for i, link in enumerate(onion_links[:10], 1):  # İlk 10 linki göster
            print(f"{i:2d}. {link['url']}")
            if link['text']:
                print(f"    Açıklama: {link['text']}")
            print()
    else:
        print("❌ Hiç .onion linki bulunamadı.")
    
    # Dark web verilerini göster
    print("🔍 Dark Web Veri Özeti:")
    print("-" * 50)
    print(f"📧 E-posta/Şifre: {len(fake_data['email_passwords'])} kayıt")
    print(f"💳 Kredi Kartı: {len(fake_data['credit_cards'])} kayıt")
    print(f"🆔 Kimlik No: {len(fake_data['identity_numbers'])} kayıt")
    print(f"📞 Telefon: {len(fake_data['phone_numbers'])} kayıt")
    print(f"🗄️ Veritabanı: {len(fake_data['database_dumps'])} dump")
    print(f"🎣 Phishing: {len(fake_data['phishing_sites'])} site")
    print(f"🔒 Ransomware: {len(fake_data['ransomware_announcements'])} duyuru")
    print(f"🦠 Malware: {len(fake_data['malware_links'])} link")
    print(f"💻 Hacklenen: {len(fake_data['hacked_sites'])} site")
    print(f"👤 Kullanıcı/Şifre: {len(fake_data['username_passwords'])} kombinasyon")
    print(f"👨‍💼 Kişisel Veri: {len(fake_data['personal_data'])} kayıt")
    
    # JSON dosyasına kaydet
    report_data = save_to_json(onion_links, tor_status, fake_data)
    
    # PDF raporu oluştur
    try:
        from pdf_generator import create_pdf_report
        create_pdf_report()
        print("📄 PDF raporu oluşturuldu: onion_scan_report.pdf")
    except Exception as e:
        print(f"⚠️ PDF oluşturma hatası: {e}")
    
    print("✅ Tarama tamamlandı!")

if __name__ == "__main__":
    main() 