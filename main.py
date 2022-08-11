import discord
import random
import pyjokes
import time
from discord.ext import commands
from keep_alive import keep_alive

TOKEN =""

client = commands.Bot(command_prefix="!")

@client.event 
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name="Ilm E-World"
    ))
    print("Bot is Ready")

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)

    if message.author == client:
        return
    if user_message.lower() == "hello" or user_message.lower() == "hi":
        await message.channel.send(f'Hello {username}!')
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
    elif user_message.lower() == "!advice":
        facts = ["If you believe , you can achieve.", "Love your family, work super hard, live your passion.", "Do good and good will come to you.", "You must be the change you wish to see in the world", "When you have a dream, you've got to grab it and never let go.", "Nothing is impossible.", "Keep your face always toward the sunshine, and shadows will fall behind you.", "You will face many defeats in life, but never let yourself be defeated.", "The greatest glory in living lies not in never falling, but in rising every time we fall.", "Life has got all those twists and turns. You've got to hold on tight and off you go.", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "You define your own life. Don't let other people write your script.", "You are never too old to set another goal or to dream a new dream.", "You don't always need a plan. Sometimes you just need to breathe, trust, let go and see what happens."]
        await message.channel.send(random.choice(facts))
        return
    elif user_message.lower() == "!motivate":
        await message.channel.send("If you believe , you can achieve.")
        time.sleep(1)
        await message.channel.send("Love your family, work super hard, live your passion.")
        time.sleep(1)
        await message.channel.send("Do good and good will come to you.")
        time.sleep(2)
        await message.channel.send("You must be the change you wish to see in the world")
        return
    if user_message.lower() == "...":
        await message.channel.send(".....")
        return

keep_alive()
client.run(TOKEN)
