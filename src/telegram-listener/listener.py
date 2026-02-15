#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram User Bot - 自動轉發訊息到 n8n
"""

import asyncio
from telethon import TelegramClient, events
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# 載入環境變數
load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
target_group = int(os.getenv('TARGET_GROUP_ID'))
n8n_webhook = os.getenv('N8N_WEBHOOK_URL')
output_channel = os.getenv('OUTPUT_CHANNEL_ID', '')  # 接收分析的頻道ID

print("🤖 Telegram Stock Analyzer User Bot")
print("="*60)
print(f"監聽群組 ID: {target_group}")
print(f"n8n Webhook: {n8n_webhook[:50]}..." if n8n_webhook else "未設定")
print("按 Ctrl+C 停止")
print("="*60 + "\n")

client = TelegramClient('session', api_id, api_hash)

# 統計
message_count = 0
success_count = 0
error_count = 0

@client.on(events.NewMessage(chats=target_group))
async def handler(event):
    global message_count, success_count, error_count
    message_count += 1
    
    # 只處理文字訊息
    if not event.message.text:
        print(f"⏭️  跳過非文字訊息")
        return
    
    # 忽略太短的訊息
    if len(event.message.text) < 20:
        print(f"⏭️  跳過太短的訊息 (< 20 字元)")
        return
    
    print(f"\n📨 處理第 {message_count} 則訊息:")
    print("-" * 60)
    print(f"時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"內容: {event.message.text[:100]}...")
    
    # 準備發送到 n8n 的資料
    payload = {
        'text': event.message.text,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'chat_name': event.chat.title if hasattr(event.chat, 'title') else '未知群組',
        'message_id': event.message.id,
        'output_channel_id': output_channel
    }
    
    try:
        # 發送到 n8n
        response = requests.post(n8n_webhook, json=payload, timeout=10)
        
        if response.status_code == 200:
            success_count += 1
            print(f"✅ 已發送到 n8n (成功: {success_count}, 失敗: {error_count})")
        else:
            error_count += 1
            print(f"❌ n8n 回應錯誤: {response.status_code}")
            
    except Exception as e:
        error_count += 1
        print(f"❌ 發送失敗: {str(e)}")
    
    print("-" * 60)

async def main():
    await client.start(phone)
    print("✅ 連接成功! 開始監聽...\n")
    
    # 獲取群組資訊
    try:
        chat = await client.get_entity(target_group)
        print(f"📊 監聽群組: {chat.title}")
        print(f"👥 成員數: {getattr(chat, 'participants_count', '未知')}\n")
    except:
        pass
    
    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n🛑 監聽已停止")
        print(f"統計: 總共 {message_count} 則, 成功 {success_count} 則, 失敗 {error_count} 則")
