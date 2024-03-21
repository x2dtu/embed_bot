import os
import re
import discord
from playwright.async_api import async_playwright

async def ifunny_embed(link: str) -> str:
    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto(link)
        
        # Select the first video tag
        video_element = await page.query_selector('video')
        
        if not video_element:
            raise ValueError(f'Could not get embed video from {link}')
        
        embed_link = await video_element.get_attribute('src')
        
        await browser.close()
        
    return embed_link

def instagram_embed(link: str) -> str:
    pattern = r"(https://(www\.)?)"

    # add 'dd' before 'instagram'
    replacement = r"\1dd"

    embed_link = re.sub(pattern, replacement, link)
    return embed_link

def vx_embed(link: str) -> str:
    pattern = r"(https://(www\.)?)"

    # add 'vx' before the domain
    replacement = r"\1vx"

    embed_link = re.sub(pattern, replacement, link)
    return embed_link

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

async def get_embed(link: str) -> str | None:
    if 'ifunny' in link:
        return await ifunny_embed(link)
    if 'tiktok' in link:
        return vx_embed(link)
    if 'twitter' in link:
        return vx_embed(link)
    if 'instagram' in link:
        return instagram_embed(link)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == client.user:
        return

    # Check if the message contains a link
    if "http://" in message.content or "https://" in message.content:
        try:
            embed_link = await get_embed(message.content)
            if embed_link:
                await message.reply(embed_link)
        except Exception as e:
            print(e)
            await message.reply("I couldn't embed this sorry master :sob:")

client.run(os.getenv('DISCORD_SECRET'))