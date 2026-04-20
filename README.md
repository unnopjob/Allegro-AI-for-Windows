# Allegro AI for Windows

AI-powered Network Troubleshooting Dashboard สำหรับ [Allegro Network Multimeter](https://www.allegro-packets.com/)  
ขับเคลื่อนด้วย **Google Gemini 2.5 Flash** — ใช้งานบน Windows ด้วย Python เพียงอย่างเดียว

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?logo=google)](https://aistudio.google.com/)

> **ไม่ต้องการ:** Node.js, npm, Visual Studio Build Tools, C++ compiler

---

## 🚀 วิธีใช้งาน (3 ขั้นตอน)

**ขั้นตอนที่ 1 — ติดตั้ง Python** (ถ้ายังไม่มี)
- ดาวน์โหลดที่ https://www.python.org/downloads/
- ⚠️ **สำคัญ:** ติ๊ก **"Add Python to PATH"** ตอนติดตั้ง

**ขั้นตอนที่ 2 — ดับเบิลคลิก `windows\start.bat`**
- ระบบจะสร้าง virtual environment และติดตั้ง packages อัตโนมัติ
- ครั้งแรกใช้เวลาประมาณ 1–2 นาที
- Browser เปิดอัตโนมัติ

**ขั้นตอนที่ 3 — เปิด http://localhost:8000**

> **ครั้งต่อไป:** ดับเบิลคลิก `start.bat` ได้เลย ไม่ต้องทำซ้ำ

---

## ⚙️ การตั้งค่าครั้งแรก

### 1. Gemini API Key
- รับฟรีที่ [Google AI Studio](https://aistudio.google.com) (ไม่ต้องใส่บัตรเครดิต)
- ไปที่หน้า **Settings** → ใส่ API Key → กด **Save & Test**
- ระบบทดสอบ Key และบันทึกอัตโนมัติ

### 2. เพิ่ม Allegro Device
- ไปที่หน้า **Devices** → กด **Add Device**
- ใส่ IP Address ของเครื่อง Allegro **(ไม่ต้องพิมพ์ https://)**
- ใส่ Username / Password
- กด **Test** เพื่อทดสอบ จากนั้นกด **Activate** เพื่อเริ่มใช้งาน

---

## ✨ ฟีเจอร์ทั้งหมด

| หน้า | ความสามารถ |
|---|---|
| 📊 **Dashboard** | Interface status real-time, bandwidth, Network Health Score (0–100), auto-refresh ทุก 10 วินาที |
| 🔍 **Analysis** | AI วิเคราะห์เครือข่าย — Overview, Security, Bandwidth, TCP Flow, Root Cause พร้อม Markdown formatting |
| 🔗 **Path & Port Check** | Ping + Traceroute + TCP port test + Allegro flow lookup ในหน้าเดียว |
| 💬 **Chat** | สนทนากับ AI พร้อมข้อมูลเครือข่ายสด (Streaming) |
| 📚 **Knowledge Base** | อัปโหลด PDF / TXT / CSV / JSON ให้ AI อ้างอิง (สูงสุด 10 MB) |
| ⚙️ **Settings** | ตั้งค่า Gemini API Key พร้อม test ทันที |
| 🌐 **EN / TH** | สลับภาษาอังกฤษ / ไทยได้ทันที ระบบจำการตั้งค่า |

---

## 📁 โครงสร้างไฟล์

```
Allegro-AI-for-Windows/
├── app/                        ← Python application
│   ├── app.py                  ← Entry point
│   ├── requirements.txt        ← Python packages
│   ├── .env.local              ← GEMINI_API_KEY (สร้างอัตโนมัติ)
│   ├── lib/
│   │   ├── db.py               ← JSON file storage
│   │   ├── allegro.py          ← Allegro API client
│   │   └── gemini.py           ← Gemini 2.5 Flash
│   ├── routers/                ← API endpoints (8 ไฟล์)
│   ├── templates/              ← HTML pages (8 หน้า)
│   └── data/                   ← ข้อมูล JSON (สร้างอัตโนมัติ)
└── windows/
    └── start.bat               ← ดับเบิลคลิกเพื่อรัน
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
| **Allegro** | Allegro Network Multimeter (firmware 4.x+) |
| **API Key** | Google Gemini — รับฟรีที่ [aistudio.google.com](https://aistudio.google.com) |

---

## ❓ แก้ปัญหา

| ปัญหา | วิธีแก้ |
|---|---|
| `Python not found` | ติดตั้ง Python ใหม่ ติ๊ก **"Add Python to PATH"** |
| `pip install failed` | รันใหม่อีกครั้ง หน้าต่างจะแสดง error message ละเอียด |
| เปิดเว็บไม่ได้ | รอสักครู่แล้วเปิด http://localhost:8000 เอง |
| API Key ไม่ผ่าน | รับ Key ใหม่ที่ [aistudio.google.com](https://aistudio.google.com) |
| ต่อ Allegro ไม่ได้ | ตรวจ IP / Username / Password และ network |
| SSL error | ปิด "Verify SSL" ในหน้า Edit Device |

---

## 📝 Changelog

### v1.3 (2025-04)
- 🌐 ระบบ 2 ภาษา EN / TH — สลับได้ทันที
- 🐛 แก้: แก้ไข Device โดยไม่กรอก Password ใหม่จะไม่ล้าง Password เดิม
- 🐛 แก้: Dashboard แสดงข้อความที่เข้าใจง่ายพร้อมลิงก์ไป Devices เมื่อยังไม่ได้ตั้งค่า
- ✨ Analysis result แสดง Markdown (headers, bold, bullet lists) แบบสวยงาม
- 🔧 start.bat เพิ่ม pip upgrade step และ verbose error output

### v1.2 (2025-03)
- ✨ Gemini SDK ใหม่: `google-genai` + model `gemini-2.5-flash`
- 🐛 รองรับ API Key format ใหม่ของ Google (`AQ.Ab...`)
- 🐛 แก้ Delete Device / Edit Device ไม่ทำงาน
- 🐛 ช่อง IP ไม่ต้องพิมพ์ `https://` แล้ว

### v1.1 (2025-02)
- ✨ Python FastAPI rewrite (ไม่ต้องการ Node.js / C++ compiler อีกต่อไป)
- ✨ Knowledge Base, Path & Port Check, AI Chat

---

## 🔗 Links

- 🛠️ **Source Code**: [github.com/unnopjob/allegro-tool](https://github.com/unnopjob/allegro-tool)
- 🤖 **Gemini API**: [aistudio.google.com](https://aistudio.google.com)
- 📡 **Allegro**: [allegro-packets.com](https://www.allegro-packets.com/)

---

## 📄 License

MIT License — ใช้งานและแก้ไขได้อิสระ
