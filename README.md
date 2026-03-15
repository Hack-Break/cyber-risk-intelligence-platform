<div align="center">

# 🛡️ CRIDAP
## Cyber Risk Intelligence & Adaptive Defense Platform

> A unified AI-powered cybersecurity system that monitors threats, correlates attack chains, scores risk dynamically, and recommends adaptive defenses — in real time.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-green?style=flat-square&logo=fastapi)
![ML](https://img.shields.io/badge/ML-Isolation%20Forest%20%7C%20Scikit--learn-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Hackathon%20Ready-orange?style=flat-square)

</div>

---

## 📌 Overview

With increasing complexity of cyber threats, organizations need intelligent systems capable of detecting attacks, prioritizing risks, and protecting sensitive data in real time.

**CRIDAP** integrates behavioural analytics, dynamic risk scoring, and incident correlation into a single unified cybersecurity solution — going beyond traditional SIEM tools by reconstructing full attack chains and recommending adaptive defenses — all visualized through a live SOC intelligence dashboard.

---

## ✨ Key Features

| Module | Description |
|--------|-------------|
| 🔎 **Multi-Layer Activity Monitor** | Ingests network, auth, and application logs |
| 🤖 **Behavioural Anomaly Detection** | ML-based detection using Isolation Forest |
| 🔗 **Attack Chain Correlation** | Links isolated events into full attack timelines |
| 📊 **Dynamic Risk Scoring** | Per-user, per-device, per-service risk scores (0–100) |
| 🔐 **Privacy Risk Monitor** | Detects unauthorized data access and exfiltration |
| ⚠️ **Adaptive Defense Advisor** | Context-aware mitigations (MFA, isolation, patching) |
| 📡 **SOC Intelligence Dashboard** | Live 3D cybersecurity visualization with real data |

---

## 🏗️ Architecture

```
Data Sources (Network / Identity / Application Logs)
                      ↓
           [ Preprocessing & Normalization Layer ]
                      ↓
       [ Behavioural ML Anomaly Detection Engine ]
                Isolation Forest | LSTM
                      ↓
         [ Alert Correlation & Chain Builder ]
                      ↓
         [ Dynamic Cyber Risk Scoring Module ]
           User Score | Device Score | Service Score
                      ↓
    [ Privacy Monitor ]     [ Defense Advisor ]
                      ↓
    [ FastAPI REST Backend · http://127.0.0.1:8000 ]
                      ↓
         [ Live SOC Intelligence Dashboard ]
```

---

## 📁 Project Structure

```
cyber-risk-platform/
├── src/
│   ├── ingestion/          # Log parsers and data collectors
│   ├── detection/          # Isolation Forest anomaly detection
│   ├── correlation/        # Attack chain correlation engine
│   ├── scoring/            # Dynamic risk scoring logic
│   ├── privacy/            # Privacy risk monitoring (5 rules)
│   ├── advisor/            # Adaptive defense recommendation engine
│   └── dashboard/          # FastAPI REST backend
├── data/
│   └── sample_logs/
│       └── sample_events.json   # 40 events · 22 entities
├── output/                 # Pipeline results (auto-generated)
├── tests/                  # 10 unit tests
├── scripts/
│   └── run_pipeline.py     # Main pipeline runner
├── docs/
│   └── architecture.md
├── index.html              # Live SOC Dashboard (frontend)
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🚀 How to Run

Follow these steps **every time** you want to start the project.

### Prerequisites

- Python 3.10+
- Git

### Step 1 — Clone the repository

```bash
git clone https://github.com/hack-break/cyber-risk-platform.git

cd cyber-risk-platform
```

### Step 2 — Create and activate virtual environment

```bash
python -m venv venv
```

**Windows (PowerShell):**
```powershell
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### Step 3 — Install dependencies

```powershell
pip install numpy pandas scikit-learn loguru fastapi uvicorn pydantic
```

### Step 4 — Run the detection pipeline

```powershell
python scripts/run_pipeline.py --log-dir data/sample_logs/
```

Expected output:
```
🛡️  Starting Cyber Risk Intelligence Pipeline
📥 Step 1: Ingesting logs...       → 40 events loaded
🤖 Step 2: Anomaly detection...    → 2 anomalies detected
🔗 Step 3: Attack chains...        → 0 chains identified
📊 Step 4: Risk scoring...         → 22 entities scored
🔐 Step 5: Privacy monitoring...   → 86 privacy signals
⚠️  Step 6: Defense advisor...     → 6 recommendations
✅ Pipeline complete. Results saved to output/results.json
```

### Step 5 — Start the API server

```powershell
uvicorn src.dashboard.api:app --reload
```

Expected output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

### Step 6 — Open the dashboard

Open `index.html` in your browser. The API status bar at the bottom will show 🟢 **API Connected** and all widgets will populate with live data.

---

## ⚡ Quick Start (One Block)

```powershell
cd cyber-risk-platform
venv\Scripts\activate
python scripts/run_pipeline.py --log-dir data/sample_logs/
uvicorn src.dashboard.api:app --reload
```

Then open `index.html` in your browser.

---

## 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Health check |
| `GET /docs` | Interactive Swagger UI |
| `GET /summary` | Pipeline run summary |
| `GET /risk-scores` | All entity risk scores |
| `GET /privacy-alerts` | Privacy risk signals |
| `GET /attack-chains` | Correlated attack chains |
| `GET /recommendations` | Defense recommendations |
| `GET /entity/{name}` | Full profile for an entity |

---

## 🧠 ML Models

| Technique | Use Case |
|-----------|----------|
| **Isolation Forest** | Unsupervised anomaly detection on tabular log data |
| **Rule-Based Correlation** | Attack chain linking from correlated alerts |
| **Statistical Thresholds** | Privacy violation signal detection |

---

## 📊 Risk Scoring Formula

Each entity is assigned a dynamic risk score from **0 to 100**:

```
Risk Score = 0.35 × Anomaly_Severity
           + 0.20 × Alert_Frequency
           + 0.15 × Privilege_Level
           + 0.20 × Data_Sensitivity_Accessed
           + 0.10 × Historical_Incident_Rate
```

| Score Range | Risk Level |
|-------------|------------|
| 80 – 100 | 🔴 CRITICAL |
| 60 – 79 | 🟠 HIGH |
| 35 – 59 | 🟡 MEDIUM |
| 0 – 34 | 🟢 LOW |

---

## 🔐 Privacy Risk Rules

| Rule | Signal | Severity |
|------|--------|----------|
| PRIV-001 | Bulk data download > 200 MB | HIGH |
| PRIV-002 | Off-hours privileged access | MEDIUM |
| PRIV-003 | New device accessing sensitive data | HIGH |
| PRIV-004 | High API call rate + bulk data transfer | CRITICAL |
| PRIV-005 | Lateral movement + data access | CRITICAL |

---

## ⚠️ Defense Recommendations

| Trigger | Action |
|---------|--------|
| Score ≥ 80 | Enforce MFA + alert SOC |
| Lateral movement detected | Isolate endpoint immediately |
| Score ≥ 60 | Force password reset |
| Bulk data exfiltration | Block session + flag for review |
| Score ≥ 35 + high privilege | Revoke elevated privileges |

---

## 📡 Sample Dataset

The platform ships with **40 real-world-simulated events** across **22 entities**:

| Entity Type | Count | Examples |
|-------------|-------|---------|
| Users | 17 | john.doe, mike.chen, carlos.mendez |
| Services | 5 | svc_api_gateway, svc_ml_pipeline |
| High-risk actors | 4 | mike.chen (score 40), raj.patel, carlos.mendez |
| Clean users | 10 | alice.smith, priya.sharma, grace.lee |

---

## ❗ Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'src'` | Run from project root folder |
| `venv\Scripts\activate` not working | Run PowerShell as Administrator |
| `uvicorn: command not found` | Run `pip install uvicorn` |
| Dashboard shows `—` dashes | Run pipeline first, then start server |
| API status bar shows 🔴 red | Start uvicorn server in a separate terminal |
| `sample_events.json` empty error | Re-download sample_events.json from repo |

---

## 🧪 Testing

```bash
pytest tests/ -v
```

All 10 tests should pass:
```
✅ TestAnomalyDetector::test_returns_list
✅ TestAnomalyDetector::test_empty_input
✅ TestAnomalyDetector::test_anomaly_has_required_fields
✅ TestRiskScorer::test_scores_computed
✅ TestRiskScorer::test_score_range
✅ TestRiskScorer::test_risk_levels_valid
✅ TestPrivacyMonitor::test_bulk_download_flagged
✅ TestPrivacyMonitor::test_clean_event_no_alerts
✅ TestDefenseAdvisor::test_critical_score_triggers_mfa
✅ TestDefenseAdvisor::test_low_score_no_critical_actions
```

---

## 📄 Abstract

With the increasing complexity of cyber threats, organizations require intelligent systems capable of detecting attacks, prioritizing risks, and protecting sensitive data in real time. This project proposes a **Cyber Risk Intelligence and Adaptive Defense Platform (CRIDAP)** that integrates behavioural analytics, risk scoring, and incident correlation into a unified cybersecurity solution.

The platform continuously monitors multi-layer system activity including network traffic, authentication events, and application usage patterns. Machine learning based anomaly detection techniques are employed to identify suspicious behaviour such as abnormal login patterns, unusual data transfers, and network reconnaissance activities. Unlike traditional alerting systems, the proposed solution correlates multiple security events to reconstruct potential **attack chains**, enabling better situational awareness for security teams.

A dynamic cyber risk scoring engine evaluates threat severity associated with users, devices, and services to support prioritized incident response. Additionally, a **privacy risk monitoring module** detects potential data exposure scenarios and unauthorized access to sensitive resources. Based on contextual threat intelligence, the platform provides adaptive defense recommendations such as enforcing MFA, isolating compromised endpoints, or prioritizing vulnerability patching.

---

## 👨‍💻 Team

| Name | Role | Links |
|------|------|-------|
| **Aishwary Vansh** | Full Stack Developer & System Architect | [LinkedIn](https://www.linkedin.com/in/aishwary-vansh/) · [GitHub](https://github.com/aishwary-vansh) |
| **Sujai Shukla** | Machine Learning Engineer & Threat Analytics Specialist | [LinkedIn](https://www.linkedin.com/in/sujai-shukla-74a3413b6) · [GitHub](https://github.com/Sujaicodes) |

---

## 🏆 Built For

This project was developed as a **hackathon submission** targeting real-world cybersecurity challenges in enterprise environments.

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-module`)
3. Commit your changes (`git commit -m 'Add new detection module'`)
4. Push to the branch (`git push origin feature/new-module`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
<b>CRIDAP · Cyber Risk Intelligence & Adaptive Defense Platform</b><br/>
Built with ❤️ for Hackathon 2025
</div>