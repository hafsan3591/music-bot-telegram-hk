"""
Apne computer ya Render ke 'Shell' tab mein chalao:
    python3 generate_session.py

ফোন নম্বর ও OTP দিন। যে স্ট্রিংটি পাবেন, সেটিই STRING_SESSION।
নিজের ব্যক্তিগত অ্যাকাউন্টের বদলে আলাদা Telegram অ্যাকাউন্ট ব্যবহার করুন।
"""

from pyrogram import Client

API_ID = int(input("API_ID দিন: "))
API_HASH = input("API_HASH দিন: ")

with Client(name="assistant_session", api_id=API_ID, api_hash=API_HASH, in_memory=True) as app:
    print("\n\n✅ আপনার STRING_SESSION নিচে দেওয়া হলো। এটি নিরাপদে .env ফাইলে রাখুন:\n")
    print(app.export_session_string())
    print("\n\n")