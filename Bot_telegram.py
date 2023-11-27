from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler

key_token = "6417310630:AAGSLKOHNH_dVQhqhXMG9Vp98-ORLdipOQ8"
user_bot = "Siswaa_igss_bot"

async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! terima kasih sudah chat dengan saya! Saya adalah Siswaa_igss_bot")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("saya adalah bot, Tolong ketik sesuatu biar bot akan membalas!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ini adalah kustom command")
    
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'hello juga!'
    if 'apa kabar' in processed:
        return 'sangan baik'
    if 'udah makan blom' in processed:
        return 'sudah'
    return 'Bot tidak mengerti yang kamu tulis....'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if user_bot in text:
            new_text: str = text.replace(user_bot, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} menyebabkan masalah {context.error}')
    
if __name__ == '__main__':
    app = Application.builder().token(key_token).build()
        
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.add_error_handler(error)
    
    print('mulai...')
    app.run_polling(poll_interval=1)
        




