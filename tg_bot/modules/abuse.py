import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Madharchod",
    " I don't have authority to chat with an asshole, Apologies",
    "╭∩╮(-_-)╭∩╮",
    "Not in a mood to abuse, I ain't gonna use my database on that shit guy.",
    "Gay is here",
    "You Betichod",
    "Ur dad lesbo",
    "Error:404 This nigga is gey af, my system can't handle such gayness. Bot Quiting",
    "U R Dad lesbo",
    "Nigga",
    "Ur dad gey bc",
    "htt bhoxdike",
    "മണ്ണുണ്ണി",
    "ഡാ പന്നക്കിളവ",
    " നിന്റെ കുഞ്ഞമ്മേടെ നായർ",
    "നിന്റെ അപ്പൂപ്പനോട്‌ പോയി പറ",
    "പോ മലരേ"
  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /abuse  🤬.
"""

__mod_name__ = "Abuse"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)
