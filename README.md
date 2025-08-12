# 🔍 Tor Onion Scanner - Advanced Dark Web Intelligence Platform

[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.7+-green?logo=python)](https://www.python.org/)
[![Tor](https://img.shields.io/badge/Tor-Network-orange?logo=tor)](https://www.torproject.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

> **🔒 Secure, Anonymous and Automated Dark Web Intelligence Platform**

This project is an advanced Docker-based system that scans, analyzes, and reports .onion sites through the Tor network. It provides maximum anonymity by using random MAC addresses on each run.

## 🌟 Key Features

### 🔐 Security & Anonymity
- **Tor SOCKS5 Proxy**: Complete anonymous connection
- **Random MAC Address**: Unique identity on each run
- **Docker Isolation**: Secure working environment
- **Automatic Cleanup**: Operations leaving no trace

### 📊 Data Collection & Analysis
- **Hidden Wiki Scanning**: Automatic collection of .onion links
- **JSON Output**: Structured data format
- **PDF Report**: Detailed analysis report with charts
- **Real-time Monitoring**: Live data flow

### 🤖 Automation & Management
- **Multiple Runs**: Batch operation support
- **System Testing**: Comprehensive validation
- **Error Handling**: Smart error catching
- **Log Management**: Detailed operation records

## 🚀 Quick Start

### 📋 Requirements

- **Docker Desktop** (Windows/Mac/Linux)
- **Python 3.7+** (for host machine)
- **Internet Connection**
- **4GB+ RAM** (recommended)

### ⚡ 5-Minute Setup

```bash
# 1. Clone the project
git clone https://github.com/yourusername/tor-onion-scanner.git
cd tor-onion-scanner

# 2. Build Docker image
docker build -t tor-onion-scanner .

# 3. Run first scan
python automation.py
```

### 🎯 Single Command Execution

```bash
# Automation mode (recommended)
python automation.py

# Manual mode
docker run --rm tor-onion-scanner:latest

# System test
python test_system.py
```

## 📁 Project Structure

```
tor-onion-scanner/
├── 📄 Dockerfile              # Docker image definition
├── 🐍 script.py               # Main scanning script
├── 📊 pdf_generator.py        # PDF report generator
├── 🤖 automation.py           # Automation script
├── 🧪 test_system.py          # System test script
├── 📖 README.md               # This file
├── 📋 requirements.txt        # Python dependencies
├── 🔧 .dockerignore           # Docker ignore file
└── 📁 outputs/                # Output files
    ├── 📄 onion_scan_results.json
    ├── 📊 onion_scan_report.pdf
    └── 🧪 test_report.json
```

## 🔧 Detailed Usage

### 🐳 Running with Docker

#### Basic Usage
```bash
# Simple execution
docker run --rm tor-onion-scanner:latest

# Get output with volume mount
docker run --rm -v $(pwd):/app/output tor-onion-scanner:latest

# With custom MAC address
docker run --rm --mac-address 00:11:22:33:44:55 tor-onion-scanner:latest
```

#### Advanced Usage
```bash
# With detailed logging
docker run --rm -v $(pwd):/app/output \
  --name tor-scanner-$(date +%s) \
  tor-onion-scanner:latest

# With network settings
docker run --rm --network host \
  --dns 8.8.8.8 \
  tor-onion-scanner:latest
```

### 🐍 Python Scripts

#### Automation Script
```bash
# Interactive mode
python automation.py

# Automatic mode (run 3 times)
echo "3" | python automation.py

# Batch mode
python automation.py --batch --runs 5
```

#### System Test
```bash
# Full test
python test_system.py

# Quick test
python test_system.py --quick

# Detailed report
python test_system.py --verbose
```

## 📊 Output Formats

### JSON Output
```json
{
  "scan_date": "2024-01-01T12:00:00.000Z",
  "tor_connection": true,
  "total_onion_links": 25,
  "onion_links": [
    {
      "url": "http://example.onion",
      "text": "Site Description",
      "found_at": "http://hiddenwiki.onion"
    }
  ],
  "scan_summary": {
    "successful_connections": 20,
    "unique_domains": 15,
    "scan_duration": "~45 seconds"
  }
}
```

### PDF Report Output
- 📈 Scan statistics chart
- 🥧 Domain distribution pie chart
- 📋 Detailed link list
- ⚠️ Security warnings
- **Example PDF Output:** [onion_scan_report.pdf](onion_scan_report.pdf)

## 🔍 MAC Address Management

### Automatic MAC Address Generation
```python
# Example MAC addresses
1c:2c:11:4a:15:3f
49:4a:ba:ae:fd:56
01:00:25:14:97:27
```

### MAC Address Verification
```bash
# Check if MAC address changed
python test_system.py --mac-test

# Test with specific MAC address
docker run --rm --mac-address 00:11:22:33:44:55 tor-onion-scanner:latest
```

## 🌐 Tor Connection Control

### Connection Test
```bash
# Test Tor connection
docker run --rm tor-onion-scanner:latest

# Look for these messages in output:
# ✅ Tor connection successful
# 🔍 Testing Tor connection...
```

### Troubleshooting
```bash
# Restart Tor service
docker run --rm tor-onion-scanner:latest sh -c "service tor restart && python3 script.py"

# Run in debug mode
docker run --rm -e TOR_DEBUG=1 tor-onion-scanner:latest
```

## ⚙️ Configuration

### Tor Settings
```bash
# Customize Tor configuration
docker run --rm -v $(pwd)/torrc:/etc/tor/torrc tor-onion-scanner:latest
```

### Python Settings
```python
# Settings in script.py
TIMEOUT = 30
MAX_RETRIES = 3
USER_AGENT = "Mozilla/5.0 (compatible; TorScanner/1.0)"
```

## 🧪 Testing & Validation

### System Test
```bash
# Full system test
python test_system.py

# Test results
{
  "test_date": "2024-01-01T12:00:00",
  "docker_image_exists": true,
  "single_run_success": true,
  "mac_test_success": true,
  "overall_status": "SUCCESS"
}
```

### Performance Test
```bash
# Speed test
time python automation.py --runs 5

# Memory usage
docker stats tor-scanner-container
```

## 🔒 Security

### Security Measures
- ✅ Anonymous connection through Tor network
- ✅ Random MAC address change
- ✅ Docker container isolation
- ✅ Automatic cleanup
- ✅ Encrypted data transfer

### Security Warnings
⚠️ **This tool is for educational and research purposes only!**

- Use within legal and ethical boundaries
- Protect your personal information
- Do not access suspicious sites
- Check local laws

## 🐛 Troubleshooting

### Common Issues

#### Docker Error
```bash
# Restart Docker service
sudo systemctl restart docker

# Clean containers
docker system prune -a
```

#### Tor Connection Error
```bash
# Check firewall settings
sudo ufw status

# Check DNS settings
nslookup google.com

# Restart container
docker run --rm --network host tor-onion-scanner:latest
```

#### MAC Address Error
```bash
# Check Docker permissions
docker run --rm --privileged tor-onion-scanner:latest

# Check MAC address format
# Format: XX:XX:XX:XX:XX:XX
```

### Debug Mode
```bash
# Run with detailed logging
docker run --rm -e DEBUG=1 tor-onion-scanner:latest

# View Tor logs
docker logs tor-scanner-container
```

## 📈 Performance

### Optimization Recommendations
- **RAM**: 4GB+ recommended
- **CPU**: 2+ cores
- **Disk**: SSD recommended
- **Network**: Stable internet connection

### Benchmark Results
```
Test Environment: Docker Desktop, 8GB RAM, SSD
- Single scan: ~30 seconds
- 10 scans: ~5 minutes
- PDF generation: ~10 seconds
- MAC change: ~1 second
```

## 🔄 Development

### Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Development Environment
```bash
# Setup development environment
git clone https://github.com/yourusername/tor-onion-scanner.git
cd tor-onion-scanner
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

## 📋 Roadmap

### 🎯 Short Term (1-3 months)
- [ ] Add web interface
- [ ] API endpoints
- [ ] More .onion sources
- [ ] Real-time monitoring
- [ ] Email reporting

### 🚀 Medium Term (3-6 months)
- [ ] Machine Learning integration
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] Cloud deployment
- [ ] Mobile app

### 🌟 Long Term (6+ months)
- [ ] AI-powered analysis
- [ ] Blockchain integration
- [ ] Enterprise features
- [ ] Global deployment
- [ ] Advanced security features

## 🤝 Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/yourusername">
        <img src="https://avatars.githubusercontent.com/yourusername" width="100px;" alt=""/>
        <br />
        <sub><b>Your Name</b></sub>
      </a>
      <br />
      <sub>🚀 Creator & Maintainer</sub>
    </td>
  </tr>
</table>

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tor Project](https://www.torproject.org/) - For anonymity
- [Docker](https://www.docker.com/) - Container technology
- [Python](https://www.python.org/) - Programming language
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Web scraping
- [ReportLab](https://www.reportlab.com/) - PDF generation

---

**🔒 Secure, Anonymous, Powerful**

</div> 
