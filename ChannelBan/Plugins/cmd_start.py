from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant



force_subhydra = "songdownload_group"



@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message: Message):
    if force_subhydra:
        try:
            user = await bot. get_chat_member(force_subhydra, message.from_user.id)
            if user.status == "kick out":
                await message.reply_text("you are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="๐๐จ๐ฎ ๐๐ซ๐ ๐๐จ๐ญ ๐๐จ๐ข๐ง๐๐ ๐ฆ๐ฒ ๐ ๐ซ๐จ๐ฎ๐ฉ\n\nโค๏ธ๐๐ข๐ซ๐ฌ๐ญ ๐ฃ๐จ๐ข๐ง ๐๐ฒ ๐๐ซ๐จ๐ฎ๐ฉ ๐ญ๐ก๐๐ง ๐๐ฅ๐ข๐๐ค ๐ฌ๐ญ๐๐ซ๐ญ ๐๐จ๐ญ๐ญ๐จ๐ง โก",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("Join My Group", url=f"t.me/{force_subhydra}")
                 ],[
                 InlineKeyboardButton("Click start Botton", url="https://t.me/AntiChannelBan_xbot?start")
                 ]]
                )
            )
            return
    await message.reply_text(
        f"""<b>Hแดส {message.from_user.first_name}!</b>
Jแดsแด แดแดแด แดแด แดแด แดสแด แดสแดแด แดษดแด แดสแดแดแดแดแด แดแด me แดแดแดษชษด, แดสแดษด I แดกษชสส สสแดแดแด แดสแด แดสแดษดษดแดสs แดสแดแด แดกสษชแดแด แดแด แดสแด แดสแดแด""",
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("๐ข Channel", url="https://t.me/Tg_Galaxy"),
           InlineKeyboardButton("โAdd Me To Groupโ", url="http://t.me/AntiChannelBan_xbot?startgroup=botstart")
           ]]
        )
    )

