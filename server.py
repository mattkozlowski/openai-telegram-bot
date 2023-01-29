import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# OpenAI API credentials
openai.api_key="HERE-YOUR-OPEN-API-TOKEN"
# Telegram Bot API credentials
token = "HERE-YOUR-TELEGRAM-API-KEY"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def ask(update, context):
    # Get the user's message
    message = update.message.text.split(" ", 1)[1]
    print(message)
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{message}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    await update.message.reply_text(f'Response {response}')

app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("ask", ask))
app.run_polling()
