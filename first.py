import discord 
import os 
from discord.ext import commands 
from dotenv import load_dotenv 

load_dotenv()
DISCORD_API_SECRET = os.getenv("DISCORD_API_KEY")
def run(): 
    intents = discord.Intents.default() 
    intents.message_content = True 
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("----------------")
        
    async def send_question(ctx, question, options):
        # Construct the message with the question and options
        message = f"**Question:** {question}\n\n"
        for index,option in enumerate(options):
            message += "\n".join(f"{index + 1}. {option}" )
            #CODE TO add reactions with the options,
        # Send the message
       
    #use the number of questions to extac tthe values from google sheets to quetsion and optiosn list, and then for loop through the rest to create the embeds 
    # Study command to display a question with options
    @bot.command()
    async def study(ctx, questionNums = 1):
        question = "What is the capital of France?"
        options = ["London", "Paris", "Berlin", "Madrid"]
        correctOption = 1
        # Create an instance of SimpleView
        view = SimpleView()
        
        # Create and send the embed with buttons
        embed = discord.Embed(
            colour=discord.Colour.orange(),
            title=f"{question}"
        )
        # Setting up the options in the description
        description = ""
        for idx, option in enumerate(options, start=1):
            description += f"{idx}. {option}\n"
        embed.description = description
        embed.set_footer(text="Select the option below")
        embed.set_author(name=f"Question {questionNums}")
    
        message = await ctx.send(embed=embed, view=view)

        
        await view.wait() 
        
        if view.choice is None:
            print("correct option was not chosen")
        elif view.choice == correctOption: 
            print("correct option was chosen")
        else:
            print("error, nothing was chosen")
        
       #await send_question(ctx, question, options)
    class SimpleView(discord.ui.View):
        choice : int = None 
        @discord.ui.button(label="1",style=discord.ButtonStyle.green)
        async def green(self, interaction:discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("first option was chosen")
            self.choice = 1
            self.stop()
            
        @discord.ui.button(label="2",style=discord.ButtonStyle.blurple)
        async def blurple(self, interaction:discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("second option was chosen")
            self.choice = 2
            self.stop()
            
        @discord.ui.button(label="3",style=discord.ButtonStyle.red)
        async def red(self, interaction:discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("third option was chosen")
            self.choice = 3
            self.stop() 
            
        @discord.ui.button(label="4",style=discord.ButtonStyle.grey)
        async def gray(self, interaction:discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("fourth option was chosen")
            self.choice = 4
            self.stop()
            

            
    bot.run()
    
if __name__ == "__main__":
    run() 