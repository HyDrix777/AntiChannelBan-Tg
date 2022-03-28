from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant



force_subhydra = "songdownload_group"



@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message: Message):
    if force_subhydra:
        try:
            user = await client. get_chat_member(force_subhydra, message.from_user.id)
            if user.status == "kick out":
                await message.reply_text("you are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="𝐘𝐨𝐮 𝐚𝐫𝐞 𝐍𝐨𝐭 𝐉𝐨𝐢𝐧𝐞𝐝 𝐦𝐲 𝐠𝐫𝐨𝐮𝐩\n\n❤️𝐅𝐢𝐫𝐬𝐭 𝐣𝐨𝐢𝐧 𝐌𝐲 𝐆𝐫𝐨𝐮𝐩 𝐭𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭𝐭𝐨𝐧 ⚡",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("Join My Group", url=f"t.me/{force_subhydra}")
                 ],[
                 InlineKeyboardButton("Click start Botton", url="https://t.me/AntiChannelBan_xbot?start")
                 ]]
                )
            )
            return
    await message.reply_text(
        f"""<b>Hᴇʏ {message.from_user.first_name}!</b>
Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴛᴏ me ᴀᴅᴍɪɴ, ᴛʜᴇɴ I ᴡɪʟʟ ʙʟᴏᴄᴋ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴛʜᴀᴛ ᴡʀɪᴛᴇ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ""",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("📢 Channel", url="https://t.me/Tg_Galaxy"),
           InlineKeyboardButton("➕Add Me To Group➕", url="http://t.me/AntiChannelBan_xbot?startgroup=botstart")
           ]]
        )
    )

