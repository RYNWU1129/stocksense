# 🤖 StockSense

AI-Powered Telegram Stock Market Analysis System

## Features

- Real-time Telegram monitoring
- AI analysis with GPT-4o-mini
- Automated insights delivery

## System Architecture

flowchart LR
    A[Telegram Groups] -->|Real-time Messages| B[Python Listener]
    B -->|HTTP POST| C[Webhook Receiver]
    C --> D[OpenAI Analysis]
    D --> E[JavaScript Formatter]
    E --> F[Telegram Bot]
    F -->|Formatted Report| G[Private Channel]
    
    style A fill:#0088cc,color:#fff
    style B fill:#3776ab,color:#fff
    style D fill:#10a37f,color:#fff
    style G fill:#0088cc,color:#fff
    style C fill:#ea4b71,color:#fff
    style E fill:#ea4b71,color:#fff
    style F fill:#ea4b71,color:#fff
 
## Tech Stack

Python • Telethon • n8n • OpenAI • Telegram Bot API

## Quick Start
```bash
git clone https://github.com/RYNWU1129/stocksense.git
cd stocksense/src/telegram-listener
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env
python3 listener.py
```

## License

MIT
