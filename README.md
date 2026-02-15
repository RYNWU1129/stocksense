# 🤖 StockSense

AI-Powered Telegram Stock Market Analysis System

## Features

- Real-time Telegram monitoring
- AI analysis with GPT-4o-mini
- Automated insights delivery

## System Architecture

graph TB
    subgraph "Data Source"
        A[📱 Telegram Groups<br/>Stock Market Discussions]
    end
    
    subgraph "Monitoring Layer<br/>WSL2 Ubuntu"
        B[🐍 Python Listener<br/>Telethon Client<br/>Async Message Capture]
    end
    
    subgraph "Automation Workflow<br/>n8n Cloud Platform"
        C[📥 Webhook Receiver<br/>POST Endpoint]
        D[🤖 OpenAI Node<br/>GPT-4o-mini<br/>Temp: 0.7 | Tokens: 1000]
        E[⚙️ JavaScript Formatter<br/>Structure & Format]
        F[📤 Telegram Bot<br/>Message Delivery]
    end
    
    subgraph "Output Destination"
        G[📊 Private Channel<br/>Structured Analysis<br/>Markdown Format]
    end
    
    A -->|Real-time Messages| B
    B -->|HTTP POST<br/>JSON Payload| C
    C -->|Message Data| D
    D -->|AI Analysis| E
    E -->|Formatted Report| F
    F -->|Send Message| G
    
    style A fill:#0088cc,stroke:#005580,stroke-width:2px,color:#fff
    style B fill:#3776ab,stroke:#2d5d8a,stroke-width:2px,color:#fff
    style D fill:#10a37f,stroke:#0d8566,stroke-width:2px,color:#fff
    style G fill:#0088cc,stroke:#005580,stroke-width:2px,color:#fff
    
    classDef n8nNode fill:#ea4b71,stroke:#c93a5f,stroke-width:2px,color:#fff
    class C,E,F n8nNode


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
