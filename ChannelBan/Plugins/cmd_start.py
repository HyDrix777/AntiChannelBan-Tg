from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant



force_subhydra = "songdownload_group"



@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message: Message):
    await message.reply_text(
        f"""<b>Hᴇʏ {message.from_user.first_name}!</b>
Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴛᴏ me ᴀᴅᴍɪɴ, ᴛʜᴇɴ I ᴡɪʟʟ ʙʟᴏᴄᴋ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴛʜᴀᴛ ᴡʀɪᴛᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ""",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("📢 Channel", url="https://t.me/Tg_Galaxy"),
           InlineKeyboardButton("➕Add Me To Group➕", url="http://t.me/AntiChannelBan_xbot?startgroup=botstart")
           ]]
        )
    )

