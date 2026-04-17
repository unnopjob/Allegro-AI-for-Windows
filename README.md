# Allegro AI for Windows

AI-powered Network Troubleshooting Dashboard สำหรับ [Allegro Network Multimeter](https://www.allegro-packets.com/)  
ขับเคลื่อนด้วย **Google Gemini 2.5 Flash** — ใช้งานบน Windows ด้วย Python

---

## 🚀 วิธีใช้งาน (3 ขั้นตอน)

**1. ติดตั้ง Python** (ถ้ายังไม่มี)
- ดาวน์โหลดที่ https://www.python.org/downloads/
- ⚠️ สำคัญ: ติ๊ก **"Add Python to PATH"** ตอนติดตั้ง

**2. ดับเบิลคลิก `windows\start.bat`**
- ระบบจะสร้าง virtual environment และติดตั้ง packages อัตโนมัติ (ครั้งแรกใช้เวลา ~2 นาที)
- Browser เปิดอัตโนมัติ

**3. เปิด http://localhost:8000**

> ครั้งต่อไป: ดับเบิลคลิก `start.bat` ได้เลย ไม่ต้องทำอะไรเพิ่ม

---

## ⚙️ การตั้งค่าครั้งแรก

### 1. Gemini API Key
- รับฟรีที่ [Google AI Studio](https://aistudio.google.com)
- ไปที่หน้า **Settings** → ใส่ API Key → กด **Save & Test**
- ระบบจะทดสอบ Key และบันทึกอัตโนมัติถ้าใช้ได้

### 2. เพิ่ม Allegro Device
- ไปที่หน้า **Devices** → กด **Add Device**
- ใส่ IP Address ของเครื่อง Allegro (ไม่ต้องใส่ https://)
- ใส่ Username / Password
- กด **Activate** เพื่อเลือกใช้งาน

---

## ✨ ฟีเจอร์

| หน้า | ความสามารถ |
|---|---|
| 📊 **Dashboard** | สถานะ Interface แบบ Real-time, Bandwidth, Network Health Score (0–100) |
| 🔍 **Analysis** | AI วิเคราะห์เครือข่าย — Overview, Security, Bandwidth, TCP Flow, Root Cause |
| 🔗 **Path & Port Check** | Ping + Traceroute + TCP Port connect test + Allegro flow lookup |
| 💬 **Chat** | สนทนากับ AI พร้อมข้อมูลเครือข่ายสด |
| 📚 **Knowledge Base** | อัปโหลด PDF/TXT/CSV/JSON ให้ AI อ้างอิง (max 10MB) |
| ⚙️ **Settings** | ตั้งค่า Gemini API Key พร้อม Test ทันที |

---

## 📁 โครงสร้างไฟล์

```
Allegro-AI-for-Windows/
├── app/                    ← Python application
│   ├── app.py              ← Entry point (python app.py)
│   ├── requirements.txt    ← Python packages
│   ├── lib/
│   │   ├── db.py           ← JSON file storage
│   │   ├── allegro.py      ← Allegro API client
│   │   └── gemini.py       ← Gemini 2.5 Flash client
│   ├── routers/            ← API endpoints (8 ไฟล์)
│   ├── templates/          ← HTML pages (8 ไฟล์)
│   └── data/               ← ข้อมูล (สร้างอัตโนมัติ)
└── windows/
    └── start.bat           ← ดับเบิลคลิกเพื่อรัน
```

---

## 🛠️ Tech Stack

| | |
|---|---|
| Backend | Python 3.11+ + FastAPI + Uvicorn |
| Frontend | HTML + Tailwind CSS CDN + Vanilla JS |
| AI | Google Gemini 2.5 Flash (`google-genai` SDK) |
| Storage | JSON files — ไม่ต้องติดตั้ง database |

---

## 📋 Requirements

| | |
|---|---|
| **Python** | 3.11 หรือสูงกว่า |
| **Allegro Device** | Allegro Network Multimeter (firmware 4.x+) |
| **API Key** | Google Gemini — รับฟรีที่ [aistudio.google.com](https://aistudio.google.com) |

> **ไม่ต้องการ:** Node.js, npm, Visual Studio Build Tools, C++ compiler

---

## ❓ แก้ปัญหา

| ปัญหา | วิธีแก้ |
|---|---|
| Python not found | ติดตั้ง Python ใหม่ ติ๊ก "Add Python to PATH" |
| pip install ช้า | รอสักครู่ ครั้งแรกต้องดาวน์โหลด ~50MB |
| เปิดหน้าเว็บไม่ได้ | รอ server start เสร็จก่อน แล้วเปิด http://localhost:8000 |
| API Key ไม่ผ่าน | ตรวจสอบ Key ที่ [aistudio.google.com](https://aistudio.google.com) |
| ต่อ Allegro ไม่ได้ | ตรวจสอบ IP, Username/Password และ Network connectivity |

---

## 📄 License

MIT License — ใช้งานและแก้ไขได้อิสระ
