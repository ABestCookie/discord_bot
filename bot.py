
# 導入Discord.py模組
import discord

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
	print(f"目前登入身份 --> {client.user}")

@client.event
# 當頻道有新訊息
async def on_message(message):
	# 排除機器人本身的訊息，避免無限循環
	if message.author == client.user:
		return
	# 新訊息包含Hello，回覆Hello, world!
	if message.content.startswith("&speak") == True:
		# 去除&speak字串
		usrmsg=message.content.lstrip("&speak")
		# 去除空格
		if usrmsg.strip().upper() == "hello":
			await message.channel.send("Hello, world!")
		elif usrmsg.strip() == "":
			await message.channel.send(f"@{message.author} 你叫我說話，我就說話了?")
			await message.channel.send("你TM甚麼都沒講，叫我叫寂寞的喔？")
			await message.channel.send("丟你老謀!") 

client.run("MTIwODM1NTQyMzg2Mjc4NDAyMQ.GJR2xc.Oo9Eyxn2SAS8yUW-Yzxx-LOmTKyca8KoxW40LY")
#MTIwODM1NTQyMzg2Mjc4NDAyMQ.GJR2xc.Oo9Eyxn2SAS8yUW-Yzxx-LOmTKyca8KoxW40LY