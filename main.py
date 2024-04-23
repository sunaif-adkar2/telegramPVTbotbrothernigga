import random
import string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from emoji import emojize

TOKEN = "6930220042:AAHEiFpKHGG6G3fGyzvZPyAlZ1O3Jm4JZ48"  # Replace this with your actual bot token
AUTHORIZED_USERS = [6996397802, 5407623254]

def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am your bot. Type /owl to generate usernames.')

def owl(update: Update, context: CallbackContext):
    """Send options to generate usernames with 3, 4, or 5 letters."""
    if update.effective_user.id in AUTHORIZED_USERS:
        buttons = [InlineKeyboardButton("Gen 3-L", callback_data="generate_3_letters"),
                   InlineKeyboardButton("Gen 4-L", callback_data="generate_4_letters"),
                   InlineKeyboardButton("Gen 5-L", callback_data="generate_5_letters")]
        keyboard = InlineKeyboardMarkup([buttons[:2], buttons[2:]])
        message_text = emojize("Choose the number of letters for your username:\n\n"
                               "3️⃣ Gen 3-L\n"
                               "4️⃣ Gen 4-L\n"
                               "5️⃣ Gen 5-L")
        update.message.reply_text(message_text, reply_markup=keyboard)
    else:
        update.message.reply_text("You are not authorized to use this bot.")

def is_reserved_username(username):
    # This function can be expanded with more comprehensive checks
    reserved_usernames = ['instagram', 'admin', 'user', 'test']  # Add more if needed
    return username.lower() in reserved_usernames

def generate_username(length):
    """Generate a random username with the specified length and a random number."""
    letters = string.ascii_lowercase
    while True:
        username = ''.join(random.choice(letters) for _ in range(length - 1))
        username += str(random.randint(0, 9))  # Add a random number at the end
        if not is_reserved_username(username):
            return username

def send_generated_username(update: Update, context: CallbackContext, length):
    """Generate a random username of specified length and send it to the user."""
    username = generate_username(length)
    update.callback_query.message.reply_text(f"Generated Instagram username: @{username}")

def button_click(update: Update, context: CallbackContext):
    """Handle button clicks."""
    query = update.callback_query
    query.answer()
    if query.data == "generate_3_letters":
        send_generated_username(update, context, 3)
    elif query.data == "generate_4_letters":
        send_generated_username(update, context, 4)
    elif query.data == "generate_5_letters":
        send_generated_username(update, context, 5)

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("owl", owl))
    dispatcher.add_handler(CallbackQueryHandler(button_click))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
