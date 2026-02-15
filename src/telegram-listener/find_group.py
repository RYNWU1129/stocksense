#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
找出所有你加入的群組和頻道 ID
"""

import asyncio
from telethon import TelegramClient
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')

print("🔍 正在連接 Telegram...")
print(f"手機號碼: {phone}")

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone)
    
    print("\n" + "="*60)
    print("📱 你的所有對話列表:")
    print("="*60 + "\n")
    
    dialogs = []
    async for dialog in client.iter_dialogs():
        dialogs.append(dialog)
    
    # 分類顯示
    print("\n🏢 群組 (Groups):")
    print("-" * 60)
    for dialog in dialogs:
        if dialog.is_group:
            print(f"  📊 {dialog.name}")
            print(f"     ID: {dialog.id}")
            print(f"     成員數: {getattr(dialog.entity, 'participants_count', '未知')}")
            print()
    
    print("\n📢 頻道 (Channels):")
    print("-" * 60)
    for dialog in dialogs:
        if dialog.is_channel and not dialog.is_group:
            print(f"  📡 {dialog.name}")
            print(f"     ID: {dialog.id}")
            print()
    
    print("="*60)
    print("\n✅ 找到你想監聽的群組了嗎?")
    print("把它的 ID 複製下來，等等會用到!\n")

with client:
    client.loop.run_until_complete(main())
