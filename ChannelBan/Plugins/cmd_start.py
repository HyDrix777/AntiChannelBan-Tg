from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.private & filters.command(["start"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hᴇʏ {message.from_user.first_name}!</b>
Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴛᴏ me ᴀᴅᴍɪɴ, ᴛʜᴇɴ I ᴡɪʟʟ ʙʟᴏᴄᴋ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴛʜᴀᴛ ᴡʀɪᴛᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ""",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("📢 Channel", url="https://t.me/Tg_Galaxy"),
           InlineKeyboardButton("➕Add Me To Group➕", url="http://t.me/AntiChannelBan_xbot?startgroup=botstart")
           ]]
        )
    )

@Client.on_message(filters.group & filters.command(["start"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hᴇʏ {message.from_user.first_name}!</b>
PM me if you have any questions on how to use me!""",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("Click me¯\_(ツ)_/¯", url="https://t.me/AntiChannelBan_xbot?start")
           ]]
        )
    )
