# Allegro AI for Windows

AI-powered Network Troubleshooting Dashboard สำหรับ [Allegro Network Multimeter](https://www.allegro-packets.com/)
ขับเคลื่อนด้วย Google Gemini 2.0 Flash — ใช้งานบน Windows ด้วย Python

---

## 🚀 วิธีใช้งาน (3 ขั้นตอน)

**1. ติดตั้ง Python** (ถ้ายังไม่มี)
- ดาวน์โหลดที่ https://www.python.org/downloads/
- ⚠️ สำคัญ: ติ๊ก **"Add Python to PATH"** ตอนติดตั้ง

**2. ดับเบิลคลิก `windows\start.bat`**
- ระบบจะติดตั้ง packages อัตโนมัติ (ครั้งแรกใช้เวลา ~1 นาที)
- Browser เปิดอัตโนมัติ

**3. เปิด http://localhost:8000**

> ครั้งต่อไป: ดับเบิลคลิก `start.bat` ได้เลย

---

## ⚙️ การตั้งค่า

### Gemini API Key
- รับฟรีที่ [Google AI Studio](https://aistudio.google.com)
- ไปที่หน้า **Settings** แล้วใส่ API Key

### เพิ่ม Allegro Device
- ไปที่หน้า **Devices** → Add Device
- ใส่ URL: `https://IP-ของเครื่อง`
- ใส่ Username / Password

---

## ✨ ฟีเจอร์

| หน้า | ความสามารถ |
|---|---|
| 📊 Dashboard | สถานะ Interface, Bandwidth, Health Score (0–100) |
| 🔍 Analysis | AI วิเคราะห์เครือข่าย — Overview, Security, Bandwidth, TCP, Root Cause |
| 🔗 Path & Port Check | Ping + Traceroute + TCP Port test |
| 💬 Chat | สนทนากับ AI พร้อมข้อมูลเครือข่ายสด |
| 📚 Knowledge Base | อัปโหลด PDF/TXT/CSV ให้ AI อ้างอิง |
| ⚙️ Settings | ตั้งค่า Gemini API Key |

---

## 📁 โครงสร้างไฟล์

```
Allegro-AI-for-Windows/
├── app/                    ← Python application
│   ├── app.py              ← รันด้วย: python app.py
│   ├── requirements.txt    ← Python packages
│   ├── lib/                ← allegro.py, gemini.py, db.py
│   ├── routers/            ← API endpoints
│   └── templates/          ← HTML pages
└── windows/
    └── start.bat           ← ดับเบิลคลิกเพื่อรัน
```

---

## 🛠️ Tech Stack

| | |
|---|---|
| Backend | Python 3.11 + FastAPI + Uvicorn |
| Frontend | HTML + Tailwind CSS CDN + Vanilla JS |
| AI | Google Gemini 2.0 Flash |
| Storage | JSON files (ไม่ต้องติดตั้ง database) |

**Requirements:** Python 3.11+ เท่านั้น — ไม่ต้องการ Node.js, C++ compiler, หรือ Visual Studio

---

## 📄 License

MIT License
