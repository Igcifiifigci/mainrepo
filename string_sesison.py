from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")
print("""𝑯𝒆𝒚𝒂❗❗❗ 𝑻𝒉𝒊𝒔 𝒊𝒔 𝑺𝒕𝒓𝒊𝒏𝒈𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒐𝒓 𝒇𝒐𝒓 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝒃𝒚 @SuperBotOT """)
print("""𝑲𝒊𝒏𝒅𝒍𝒚 𝒆𝒏𝒕𝒆𝒓 𝒕𝒉𝒆 𝒅𝒆𝒕𝒂𝒊𝒍𝒔 𝒂𝒔𝒌𝒆𝒅 𝒕𝒐 𝒑𝒓𝒐𝒄𝒆𝒆𝒅 ❗❗ """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "𝑺𝒕𝒓𝒊𝒏𝒈𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝒘𝒂𝒔 𝒔𝒆𝒏𝒕 𝒕𝒐 𝒚𝒐𝒖𝒓 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑺𝒂𝒗𝒆𝒅 𝑴𝒆𝒔𝒔𝒂𝒈𝒆𝒔, 𝑮𝒐 𝒂𝒏𝒅 𝒈𝒆𝒕 𝒊𝒕, 𝒂𝒏𝒅 𝑲𝒆𝒆𝒑 𝒊𝒕 𝑺𝒂𝒇𝒆 𝒂𝒏𝒅 𝑫𝒐𝒏❜𝒕 𝒓𝒆𝒗𝒆𝒂𝒍 𝒕𝒐 𝒐𝒕𝒉𝒆𝒓𝒔. "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"𝑯𝒆𝒓𝒆 𝒊𝒔 𝒕𝒉𝒆 𝑺𝒕𝒓𝒊𝒏𝒈𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝒇𝒐𝒓 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕\n(**𝙏𝙖𝙥 𝙤𝙣 𝙩𝙝𝙚 𝙎𝙩𝙧𝙞𝙣𝙜 𝙩𝙤 𝘾𝙤𝙥𝙮 𝙄𝙩**)👇\n\n`{session}`\n\n𝑽𝒊𝒔𝒊𝒕 @SuperBotOT 𝒇𝒐𝒓 𝒂𝒏𝒚 𝒒𝒖𝒆𝒓𝒊𝒆𝒔 𝒐𝒓 𝒉𝒆𝒍𝒑."
   )
 except Exception as e:
  print(str(e))
  print(
      "\n⚠️ 𝐖𝐚𝐫𝐧𝐢𝐧𝐠 ⚠️\n𝑾𝒓𝒐𝒏𝒈 𝑷𝒉𝒐𝒏𝒆 𝑵𝒐. 𝒑𝒓𝒐𝒗𝒊𝒅𝒆𝒅 ❗❗ \n𝑴𝒂𝒌𝒆 𝒔𝒖𝒓𝒆 𝒕𝒉𝒂𝒕 𝒕𝒉𝒆 𝒑𝒓𝒐𝒗𝒊𝒅𝒆𝒅 𝑷𝒉𝒐𝒏𝒆 𝑵𝒐. 𝒊𝒔 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑪𝒐𝒖𝒏𝒕𝒓𝒚 𝑪𝒐𝒅𝒆. 𝙀𝙭𝙖𝙢𝙥𝙡𝙚 : +91 9*6*3 4*2*1\n\n𝑲𝒊𝒏𝒅𝒍𝒚 𝑹𝒆𝑻𝒓𝒚"
  )
  print("")
  continue
 break
