from discord.ext import commands
from discord.ext.commands.core import guild_only
from discord.message import DeletedReferencedMessage

bot = commands.Bot(command_prefix="##", case_insensitive=True, name="ChatNote")


        ######ids adms####


bot = commands.Bot(command_prefix="##", case_insensitive=True, name="ChatNote")

class ChatNoteCommands(commands.Cog, name="ChatNote"):
    @commands.command(
        help="Adds a new note to your current notebook, or the specified notebook",
        brief="Adds a note to a notebook",
        pass_context=True
    )
    async def note(self, ctx, *, text):
        note_text = text.strip()
        await ctx.channel.send("Noted: " + note_text)




    ################################333333333

@bot.event
async def on_message(message):


        ######ids adms####
    if message.author.id == 997129721550753862: #este id bot
        return
    ###if message.author.id == 591790331947778086: #mi id
       ### return
#######################################################config
    user = message.author
    user_id = message.author.id
    channel = message.channel.id
    content = message.content
    channel = bot.get_channel(997127090568712282)###va
    if message.content:
     await channel.send(f"{content}")
     await bot.process_commands(message)
     return



################################

bot.run('OTk3MTI5NzIxNTUwNzUzODYy.GIvIEs.Ma5k4M-KK1SdJf4uJIGEMNVDMPW2rCG95jw7Y4')
