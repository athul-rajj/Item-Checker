import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from text_Finder import Finder
import time

client = commands.Bot(command_prefix='!')
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("log-level=3")
driver=webdriver.Chrome(r"C:/Users/athul/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def search(ctx, arg):
    counter = 370
    status = True
    while status:
        driver.get("https://api.bestbuy.com/v1/products((search=" + str(arg) +"))?apiKey=fbHpo1XU31MYqyDvPNeczIzQ&sort=onlineAvailability.asc&show=orderable,name,addToCartUrl&pageSize=24&format=json")

        avail = []
        names = []
        url = []
        stock = []
        o = 0
        ns = 0
        us = 0
        page=driver.page_source
        page = Finder.noEnd(str(page), '"products":[')
        for c, v in enumerate(str(page)):
            if page[c:c+9] == 'orderable':
                o = c + 12
            if page[c:c+4] == 'Sold':
                avail.append("Sold Out")
            elif page[c:c+9] == 'Available':
                avail.append("In Stock")

        for c, v in enumerate(str(page)):
            if page[c:c+4] == "name":
                ns = c + 7
            if page[c:c+5] == "addTo":
                names.append(str(page)[ns:c-3])

        for c, v in enumerate(str(page)):
            if page[c:c+12] == "addToCartUrl":
                us = c + 15
            if page[c:c+4] == "cart":
                url.append(str(page)[us:c+4])

        for c, v in enumerate(avail):
            stock.append("\nNAME: " + names[c] + "\nSTOCK: " + avail[c] + "\nLINK: " + url[c])

        time.sleep(2)

        if counter > 360:
            embed=discord.Embed(title="STOCK CHECKER", color=0xEC5252)
            #description="These are probably not in stock"
            for i in stock:
                embed.add_field(name="-", value=i, inline=False)
            embed.set_footer(text="We are not associated with Bestbuy")
            await ctx.send(embed=embed)
            counter = 0

        for c, v in enumerate(avail):
            if v == "In Stock":
                embed=discord.Embed(title="STOCK CHECKER", description="BUY NOW", color=0xEC5252)
                embed.add_field(name="ITEM: ", value=names[c], inline=False)
                embed.add_field(name="IN STOCK: ", value=url[c], inline=False)
                #embed.set_footer(text="If we are still pinging, the cards are still in stock")
                await ctx.send(embed=embed)
                await ctx.channel.send("@everyone")
                #check = False
                status = False

        counter += 1

client.run('ODQyMTM0Mzk3NTE1MDcxNTE4.YJw4xg.lBgTauBk_UdQowWZEgo-U9Pq6dQ')
