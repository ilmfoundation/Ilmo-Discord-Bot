import discord
import random
import pyjokes
import time
from keep_alive import keep_alive

TOKEN =""

client = discord.Client()

@client.event
async def on_ready():
    print('We have loged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)

    if message.author == client:
        return
        
    if user_message.lower() == "bye":
        await message.channel.send(f'See you later {username}!')
        return
    elif user_message.lower() == "!random":
        response = f'This is your random number: {random.randrange(10000)}'
        await message.channel.send(response)
        return
    elif user_message.lower() == "!important":
        await message.channel.send("@everyone Come here it is important")
        return
    elif user_message.lower() == "lol":
        await message.channel.send("lol HaHaHa")
        return
    elif user_message.lower() == "xd":
        await message.channel.send("HaHaHa")
        return
    elif user_message.lower() == "!help":
        await message.channel.send("if you need any help, please contact the owner of this server")
        return
    elif user_message.lower() == "!gif":
        await message.channel.send(random.choice(["https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ", "https://tenor.com/view/liujun-junliu-gif-24362435", "https://tenor.com/view/yes-will-ferrell-awesome-gif-14597941", "https://tenor.com/view/cat-high-five-yes-oh-hell-gif-14324160", "https://tenor.com/view/high-five-top-gun-tom-cruise-gif-9817538", "https://tenor.com/view/yay-omg-clap-excited-gif-13535331", "https://tenor.com/view/yay-gif-24172682"]))
        return
    elif user_message.lower() == "!rickroll":
        await message.channel.send("https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ")
        return
    elif user_message.lower() == "ping":
        await message.channel.send("pong")
        return
    elif user_message.lower() == "ting":
        await message.channel.send("tong")
        return
    elif user_message.lower() == "!joke":
        joke = pyjokes.get_joke()
        await message.channel.send(joke)
        return
    elif user_message.lower() == "!fact":
        facts = ["It's legal for anyone over 5 years old to drink alcohol in the UK.", "Jupiter has over 70 moons.", "A jail for polar bears exists.", "Camels store water their bloodstream, not their hump which is fatty tissue.", "Oxford University is older than the Aztec Empire", "Nintendo has existed as a company since 1889", "Earth used to be purple.", "Most of the visible stars you see in the night sky are binary stars - two stars orbiting each other.", "Venus spins the wrong way compared to other planets.", "In a room with just 23 people, there’s a 50-50 chance that at least two people have the same birthday.", "Babies have 300 bones when born while an adult only has 206 bones.", "A woodpecker's tongue wraps around its brain.", "A Japanese company gives its non-smoking employees 6 extra vacation days to compensate for smoking breaks.", "The national animal of Scotland is the unicorn."]
        await message.channel.send(random.choice(facts))
        return
    elif user_message.lower() == "!motivate":
        await message.channel.send("You are awesome.")
        time.sleep(1)
        await message.channel.send("You are great.")
        time.sleep(1)
        await message.channel.send("You can do anything you want.")
        time.sleep(2)
        await message.channel.send("You are powerful.")
        return
    if user_message.lower() == "...":
        await message.channel.send(".....")
        return

keep_alive()
client.run(TOKEN)
