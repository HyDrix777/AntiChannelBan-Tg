from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hᴇʏ {message.from_user.first_name}!</b>
Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ, ᴀɴᴅ I ᴡɪʟʟ ʙʟᴏᴄᴋ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴛʜᴀᴛ ᴡʀɪᴛᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ""",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("📢 Channel", url="https://t.me/Tg_Galaxy"),
           InlineKeyboardButton("➕Add Me To Group➕", url="http://t.me/AntiChannelBan_x2bot?startgroup=botstart")
           ]]
        )
    )
