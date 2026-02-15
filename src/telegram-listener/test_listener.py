#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
測試監聽器 - 監聽群組訊息並顯示
"""

import asyncio
from telethon import TelegramClient, events
import os
from dotenv import load_dotenv
from datetime import datetime

# 載入環境變數
load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
target_group = int(os.getenv('TARGET_GROUP_ID'))

print("🤖 User Bot 測試程式")
print("="*60)
print(f"監聽群組 ID: {target_group}")
print("按 Ctrl+C 停止")
print("="*60 + "\n")

client = TelegramClient('session', api_id, api_hash)

# 計數器
message_count = 0

@client.on(events.NewMessage(chats=target_group))
async def handler(event):
    global message_count
    message_count += 1
    
    print(f"\n📨 收到第 {message_count} 則訊息:")
    print("-" * 60)
    print(f"時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"發送者: {event.sender.first_name if event.sender else '未知'}")
    print(f"內容: {event.message.text[:200] if event.message.text else '[非文字訊息]'}...")
    print("-" * 60)

async def main():
    await client.start(phone)
    print("✅ 連接成功! 開始監聽...\n")
    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n🛑 監聽已停止")
        print(f"總共收到 {message_count} 則訊息")
