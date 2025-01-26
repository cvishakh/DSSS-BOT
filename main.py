from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

#Load the TinyLlama model and text generation pipeline
MODEL = "PY007/TinyLlama-1.1B-Chat-v0.1"
from transformers import pipeline
pipe = pipeline(
    "text-generation",
    model=MODEL,
    torch_dtype="auto",  #Automatically use the appropriate dtype
    device=-1  #Use CPU, for GPU =0
)

#Telegram bot API Token
API_TOKEN = "Replace with your token key"

#Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your AI assistant. Start asking!")

#Message handler for user input
async def process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text  # Extract the user message
    print(f"User Message: {user_message}")

    #Generate a response using the model
    prompt = f"### Human: {user_message}\n### Assistant:"
    response = pipe(
        prompt,
        do_sample=True,
        top_k=70,
        top_p=0.85,
        repetition_penalty=1.1,
        max_new_tokens=200,
    )

    #Extract and send the generated reply
    bot_reply = response[0]["generated_text"].split("### Assistant:")[-1].strip()
    await update.message.reply_text(bot_reply)

#Main function to set up and run the bot
def main():
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process))
    app.run_polling()

#Run the bot
if __name__ == "__main__":
    main()
