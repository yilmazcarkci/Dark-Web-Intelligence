#!/usr/bin/env python3
import json
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

def create_charts(data):
    """Create charts and save as files (English)"""
    charts = {}
    
    # 1. Onion link count chart
    plt.figure(figsize=(10, 6))
    categories = ['Total Links', 'Unique Domains', 'Successful Connections']
    values = [
        data['total_onion_links'],
        data['scan_summary']['unique_domains'],
        data['scan_summary']['successful_connections']
    ]
    
    bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    plt.title('Onion Scan Statistics', fontsize=16, fontweight='bold')
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45)
    
    # Değerleri barların üzerine yaz
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                str(value), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('onion_stats.png', dpi=300, bbox_inches='tight')
    plt.close()
    charts['stats'] = 'onion_stats.png'
    
    # 2. Dark Web data distribution chart
    if 'dark_web_data' in data:
        dark_data = data['dark_web_data']
        categories = list(dark_data.keys())
        values = [len(dark_data[cat]) for cat in categories]
        
        plt.figure(figsize=(12, 8))
        bars = plt.bar(range(len(categories)), values, color=plt.cm.Set3(range(len(categories))))
        plt.title('Dark Web Data Distribution', fontsize=16, fontweight='bold')
        plt.ylabel('Record Count', fontsize=12)
        plt.xticks(range(len(categories)), [cat.replace('_', ' ').title() for cat in categories], rotation=45, ha='right')
        
        # Değerleri barların üzerine yaz
        for i, v in enumerate(values):
            plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('dark_web_data.png', dpi=300, bbox_inches='tight')
        plt.close()
        charts['dark_web'] = 'dark_web_data.png'
    
    return charts

def create_dark_web_tables(dark_data):
    """Create dark web data tables in English"""
    tables = []
    
    # Email/Password table
    if dark_data.get('email_passwords'):
        email_data = [['Email', 'Password', 'Source']]
        for item in dark_data['email_passwords'][:5]:  # İlk 5 kayıt
            email_data.append([item['email'], item['password'], item['source']])
        
        email_table = Table(email_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
        email_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        tables.append(('📧 Email Addresses and Passwords', email_table))
    
    # Credit card table
    if dark_data.get('credit_cards'):
        card_data = [['Card Number', 'Expiry', 'Bank']]
        for item in dark_data['credit_cards']:
            card_data.append([item['number'], item['expiry'], item['bank']])
        
        card_table = Table(card_data, colWidths=[2*inch, 1*inch, 2*inch])
        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        tables.append(('💳 Credit Card Numbers', card_table))
    
    # Identity numbers table
    if dark_data.get('identity_numbers'):
        id_data = [['Type', 'Number', 'Country']]
        for item in dark_data['identity_numbers']:
            id_data.append([item['type'], item['number'], item['country']])
        
        id_table = Table(id_data, colWidths=[1*inch, 2*inch, 1*inch])
        id_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        tables.append(('🆔 Identity Numbers', id_table))
    
    # Phishing sites table
    if dark_data.get('phishing_sites'):
        phish_data = [['URL', 'Target', 'Status']]
        for item in dark_data['phishing_sites']:
            phish_data.append([item['url'], item['target'], item['status']])
        
        phish_table = Table(phish_data, colWidths=[2.5*inch, 1.5*inch, 1*inch])
        phish_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        tables.append(('🎣 Phishing Sites', phish_table))
    
    # Ransomware announcements table
    if dark_data.get('ransomware_announcements'):
        ransom_data = [['Group', 'Victim', 'Demand']]
        for item in dark_data['ransomware_announcements']:
            ransom_data.append([item['group'], item['victim'], item['demand']])
        
        ransom_table = Table(ransom_data, colWidths=[1.5*inch, 2*inch, 1.5*inch])
        ransom_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.red),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        tables.append(('🔒 Ransomware Announcements', ransom_table))
    
    return tables

def create_pdf_report(json_file="onion_scan_results.json", output_file="onion_scan_report.pdf"):
    """Create PDF report in English"""
    
    # JSON dosyasını oku
    if not os.path.exists(json_file):
        print(f"❌ {json_file} not found!")
        return False
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # PDF dokümanı oluştur
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    story = []
    
    # Stil tanımları
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.darkred
    )
    
    normal_style = styles['Normal']
    
    # Başlık
    story.append(Paragraph("🔍 Tor Onion Scanner - Dark Web Intelligence Report", title_style))
    story.append(Spacer(1, 20))
    
    # Tarama bilgileri
    story.append(Paragraph("📊 Scan Summary", heading_style))
    
    scan_info = [
        ["Scan Date", data['scan_date'][:19].replace('T', ' ')],
        ["Tor Connection", "✅ Successful" if data['tor_connection'] else "❌ Failed"],
        ["Total Onion Links", str(data['total_onion_links'])],
        ["Unique Domains", str(data['scan_summary']['unique_domains'])],
        ["Successful Connections", str(data['scan_summary']['successful_connections'])],
        ["Scan Duration", data['scan_summary']['scan_duration']]
    ]
    
    scan_table = Table(scan_info, colWidths=[2*inch, 3*inch])
    scan_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(scan_table)
    story.append(Spacer(1, 20))
    
    # Grafikleri oluştur
    charts = create_charts(data)
    
    # İstatistik grafiği
    if 'stats' in charts:
        story.append(Paragraph("📈 Scan Statistics", heading_style))
        story.append(Paragraph(f"<img src='{charts['stats']}' width='400' height='240'/>", normal_style))
        story.append(Spacer(1, 20))
    
    # Dark Web veri grafiği
    if 'dark_web' in charts:
        story.append(Paragraph("🌐 Dark Web Data Distribution", heading_style))
        story.append(Paragraph(f"<img src='{charts['dark_web']}' width='400' height='320'/>", normal_style))
        story.append(Spacer(1, 20))
    
    # Dark Web verileri tabloları
    if 'dark_web_data' in data:
        story.append(PageBreak())
        story.append(Paragraph("🔍 Dark Web Data Analysis", heading_style))
        story.append(Spacer(1, 12))
        
        dark_tables = create_dark_web_tables(data['dark_web_data'])
        
        for title, table in dark_tables:
            story.append(Paragraph(title, heading_style))
            story.append(table)
            story.append(Spacer(1, 12))
    
    # Onion linkleri listesi
    story.append(PageBreak())
    story.append(Paragraph("🔗 Found Onion Links", heading_style))
    story.append(Spacer(1, 12))
    
    # İlk 20 linki tablo halinde göster
    table_data = [["#", "URL", "Description"]]
    
    for i, link in enumerate(data['onion_links'][:20], 1):
        url = link['url'][:50] + "..." if len(link['url']) > 50 else link['url']
        text = link['text'][:30] + "..." if len(link['text']) > 30 else link['text']
        table_data.append([str(i), url, text])
    
    link_table = Table(table_data, colWidths=[0.5*inch, 3*inch, 2*inch])
    link_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
    ]))
    
    story.append(link_table)
    
    if len(data['onion_links']) > 20:
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"... and {len(data['onion_links']) - 20} more links", normal_style))
    
    # Güvenlik notu
    story.append(PageBreak())
    story.append(Paragraph("⚠️ Security Warning", heading_style))
    story.append(Paragraph(
        """
        This report is for educational and research purposes only. The data shown are fake and do not represent real individuals. 
        The content of the found links has not been checked and may be potentially dangerous. Before accessing these links, 
        take your security precautions and do not forget your legal responsibilities.
        """, normal_style))
    
    # PDF'i oluştur
    doc.build(story)
    
    # Geçici dosyaları temizle
    for chart_file in charts.values():
        if os.path.exists(chart_file):
            os.remove(chart_file)
    
    print(f"✅ PDF report generated: {output_file}")
    return True

if __name__ == "__main__":
    create_pdf_report() 