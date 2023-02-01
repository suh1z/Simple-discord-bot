import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!ping'):
        await message.channel.send('Pong!')

    if message.content.startswith('!say'):
        message_content = message.content[len('!say'):].strip()
        await message.channel.send(message_content)
        
    if message.content.startswith('!kick'):
        if not message.author.guild_permissions.administrator:
            await message.channel.send("You don't have the permission to use this command.")
            return

        user_mention = message.content[len('!kick'):].strip()
        if not user_mention:
            await message.channel.send("Please mention a user to kick.")
            return

        user = message.guild.get_member(int(user_mention[2:-1]))
        if not user:
            await message.channel.send("User not found.")
            return

        await user.kick()
        await message.channel.send(f"{user.name} was kicked.")

    if message.content.startswith('!ban'):
        if not message.author.guild_permissions.administrator:
            await message.channel.send("You don't have the permission to use this command.")
            return

        user_mention = message.content[len('!ban'):].strip()
        if not user_mention:
            await message.channel.send("Please mention a user to ban.")
            return

        user = message.guild.get_member(int(user_mention[2:-1]))
        if not user:
            await message.channel.send("User not found.")
            return

        await user.ban()
        await message.channel.send(f"{user.name} was banned.")

client.run('YOUR_DISCORD_BOT_TOKEN')
