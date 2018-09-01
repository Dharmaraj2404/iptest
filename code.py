# Innocent Promotion Bot Source Code
# Legal Property of Innocent Promotions ™
# Founder: @dharmraj_24
# python-telegram-bot

# V1:
# Basic Functions
# On-time when required
# Post messages on registered channels
# Uses Channel @username as User ID
# Developer-Only commands

# Importing Modules
try:
    import os, telegram, time, sys, logging
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
    from telegram.ext.dispatcher import run_async
    from functools import wraps
    from pprint import pprint
except ImportError as e:
    print("Problem: ",e)
    exit()

# Bot Data:

botname  = 'Innocent Promotion Bot'
botver   = 'v1'
bottoken = '612573309:AAGAAuScxQlF21mw0kPvNyk9PqarnhgyrFs'   # <-- Bot Token



# Polling Setup
try:
    updater = Updater(bottoken)
except ValueError as e:
    print("Please insert your Bot Token!")
    exit()

# Handling Command
dispatcher = updater.dispatcher

#logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

user_data     = {}
vip_developer = 293125876

#Commands
@run_async
def start(bot, update):
    if update.message.chat_id < 0:
        bot.send_message(chat_id=update.message.chat_id, text="Kindly use PM", parse_mode=telegram.ParseMode.MARKDOWN)
        return
    user = "{}".format(update.effective_user.username)

# Message Content
    msg = "Hello @"+user+" ! \n"
    msg+= "Kindly use /help for more details on how to promote your Channel!"
    bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)


@run_async
def help(bot, update):
    if update.message.chat_id < 0:
        bot.send_message(chat_id=update.message.chat_id, text="Kindly use PM! ", parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #user Data
    msg = "To register your Channel, follow the below steps: \n"
    msg+= "Type `/register` followed by the data below in the same message \n"
    msg+= "#username - followed by `@username` of the channel \n"
    msg+= "#desc - Description of Channel in max 5 words \n"
    msg+= "#subs - Current number of Subscribers \n"
    msg+= " \n"
    msg+= " \n"
    msg+= "For example: \n"
    msg+= "`/register` \n"
    msg+= "#username @InnocentPromotions \n"
    msg+= "#desc Promoting Channel \n"
    msg+= "#subs 100 \n"
    bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)


@run_async
def register(bot, update, args):
    if update.message.chat_id < 0:
        bot.send_message(chat_id=update.message.chat_id, text="Kindly use PM! Registering from groups is currently unavailable.", parse_mode=telegram.ParseMode.MARKDOWN)
        return

    user_username  = update.effective_user.username
    user_chatid    = update.message.chat_id
    user_firstname = update.message.from_user.first_name

    try:
        channel_data = args[0]
    except IndexError as e:
        update.message.reply_text("Please enter all the required details! For more details refer /help")
        return

    if str(user_chatid) in user_data:
        bot.send_message(chat_id=update.message.chat_id, text="Your Channel has been registered!", parse_mode=telegram.ParseMode.MARKDOWN)
        return

    channel_data[str(user_chatid)] = {"user_firstname": str(user_firstname), "user_username": user_username, "channel_data": channel_data}

# Message to be sent to Owner
    msg  = "Registered by: "+user_username+"/n"
    msg += "Channel details: /n"
    msg += " "+channel_data+ "/n"

    print(channel_data)
    print("\n")
    print(msg)

    # Sending message to admins
    bot.send_message(chat_id=293125876, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    return

###################################
@run_async
#register command function
def regi(bot, update, args):
	#avoid request from grup (PM Only)
	if update.message.chat_id < 0:
		return
	#user data
	user_username = update.effective_user.username
	user_chatid   = update.message.chat_id
	user_firstname= update.message.from_user.first_name
	try:
		user_pubg_ign = args[0]
	except IndexError as e:
		update.message.reply_text("Please input your PUBG IGN!")
		return

	#filter for avoid spammer
	if len(user_pubg_ign) > 20:
		bot.send_message(chat_id=update.message.chat_id, text="*Please don't make spam in this bot!*", parse_mode=telegram.ParseMode.MARKDOWN)
		return

	#check same data:
	if str(user_chatid) in users_data:
		bot.send_message(chat_id=update.message.chat_id, text="*You has been registered!*", parse_mode=telegram.ParseMode.MARKDOWN)
		return

	#send user data to users_data
	users_data[str(user_chatid)]= {"user_firstname":str(user_firstname), "user_username":user_username, "user_pubg_ign":user_pubg_ign}

	#make report message about user's biodata
	msg = "PUBG PLAYER: "+user_firstname+"\n"
	msg+= "USERNAME  : @"+user_username+"\n"
	msg+= "PUBG IGN  : "+user_pubg_ign+"\n"

	print(users_data)
	print("\n")
	print(msg)

	#INLINE KEYBOARD


	#send message to user
	bot.send_message(chat_id=update.message.chat_id, text=msg)


###################################






# Configure Command
start_handler      = CommandHandler('start', start)
help_handler       = CommandHandler('help', help)
register_handler   = CommandHandler('register', register)
regi_handler       = CommandHandler('regi', regi)

# Set Command
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(register_handler)
dispatcher.add_handler(regi_handler)

# Start Polling
print(botname,' ',botver,' : Started Succesfully!')
updater.start_polling()

