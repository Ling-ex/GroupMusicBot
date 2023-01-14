import yt_dlp
from pyrogram import filters
from pyrogram import Client
from Yukki import app, SUDOERS, BOT_ID, BOT_USERNAME, OWNER
from Yukki import dbb, app, BOT_USERNAME, BOT_ID, ASSID, ASSNAME, ASSUSERNAME
from ..YukkiUtilities.helpers.inline import start_keyboard, personal_markup
from ..YukkiUtilities.helpers.thumbnails import down_thumb
from ..YukkiUtilities.helpers.ytdl import ytdl_opts 
from ..YukkiUtilities.helpers.filters import command
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Yukki.YukkiUtilities.database.chats import (get_served_chats, is_served_chat, add_served_chat, get_served_chats)
from Yukki.YukkiUtilities.database.queue import (is_active_chat, add_active_chat, remove_active_chat, music_on, is_music_playing, music_off)
from Yukki.YukkiUtilities.database.sudo import (get_sudoers, get_sudoers, remove_sudo)

def start_pannel():  
    buttons  = [
            [
                InlineKeyboardButton(text="📚 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", url="https://telegra.ph/HYPER-ROBOT-01-12-2")
            ],
            [ 
                InlineKeyboardButton(text="📣 ᴄʜᴀɴɴᴇʟ", url="https://t.me/storyQi"),
                InlineKeyboardButton(text="💭 ɢʀᴏᴜᴘꜱ", url="https://t.me/HyperSupportQ")
            ],
    ]
    return "✨  **Welcome to Hyper Robot.**", buttons

pstart_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴀ ɢʀᴏᴜᴘ ➕", url="http://t.me/Ling_Musik_Bot?startgroup=new")
                ],[
                    InlineKeyboardButton(
                        "📚 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", url="https://telegra.ph/HYPER-ROBOT-01-12-2"),
                    InlineKeyboardButton(
                        "♥️ ᴅᴏɴᴀᴛᴇ", url="https://telegra.ph/file/fec1a0e93ccf3f52806f4.jpg")
                ],[
                    InlineKeyboardButton(
                        "👥 ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘꜱ", url="https://t.me/HyperSupportQ"), 
                    InlineKeyboardButton(
                        "📣 ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url="https://t.me/storyQi")
                ],[
                    InlineKeyboardButton(
                        "❓ ꜱᴇᴛᴜᴘ ɢᴜɪᴅᴇ", url="https://telegra.ph/HYPER-ROBOT-01-13")
                ]
            ]
        )

welcome_captcha_group = 2
@app.on_message(filters.new_chat_members, group=welcome_captcha_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(chat_id):
        await message.reply_text(f"❌ **not in allowed chat**\n\nHyper Robot is only for allowed chats, ask any sudo user to allow your chat.\n\ncheck sudo user list [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)")
        return await app.leave_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id in OWNER:
                return await message.reply_text(f"💡 Announcement, My Owner [{member.mention}] has joined this group.")
            if member.id in SUDOERS:
                return await message.reply_text(f"💡 Announcement, The Sudo member [{member.mention}] has joined this group.")
            if member.id == ASSID:
                await remove_active_chat(chat_id)
            if member.id == BOT_ID:
                out = start_pannel()
                await message.reply_text(f"❤️ **Thanks for adding me to the group !**\n\n**Promote me as administrator of the group, otherwise I will not be able to work properly.", reply_markup=InlineKeyboardMarkup(out[1]))
                return
        except:
            return

@Client.on_message(filters.group & filters.command(["mstart", "mhelp"]))
async def mstart(_, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(chat_id):
        await message.reply_text(f"❌ **not in allowed chat**\n\nHyper Robot is only for allowed chats, ask any sudo user to allow your chat.\n\ncheck sudo user list [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)")
        return await app.leave_chat(chat_id)
    out = start_pannel()
    await message.reply_text(f"✨ Hello {message.from_user.mention}, i'm a Hyper Robot.\n\n💭 Make me admin in your group so I can play music, otherwise you can't use my service.", reply_markup=InlineKeyboardMarkup(out[1]))
    return
        
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def play(_, message: Message):
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "["+user_name+"](tg://user?id="+str(user_id)+")" 
        await app.send_message(message.chat.id,
            text=f"✨ Welcome {rpk} !\n\n💭 [Hʏᴘᴇʀ Aꜱꜱɪꜱᴛᴀɴᴛ 🇮🇩](https://t.me/Ling_Musik_Bot) **allows** you to **play music** on **Groups** through the new **Telegram's video chats** feature !\n\n💡 **Find out** all the **Bot's commands** and how they work by clicking on the » 📚 **ᴄᴏᴍᴍᴀɴᴅꜱ** button!",
            parse_mode="markdown",
            reply_markup=pstart_markup,
            reply_to_message_id=message.message_id,
            disable_web_page_preview=True
        )
    elif len(message.command) == 2:                                                           
        query = message.text.split(None, 1)[1]
        f1 = (query[0])
        f2 = (query[1])
        f3 = (query[2])
        finxx = (f"{f1}{f2}{f3}")
        if str(finxx) == "inf":
            query = ((str(query)).replace("info_","", 1))
            query = (f"https://www.youtube.com/watch?v={query}")
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                x = ytdl.extract_info(query, download=False)
            thumbnail = (x["thumbnail"])
            searched_text = f"""
💡 **Track Informations**

🏷 **Name:** {x["title"]}
⏱ **Duration:** {round(x["duration"] / 60)} min(s)
👀 **Views:** `{x["view_count"]}`
⭐️ **Ratings:** {x["average_rating"]}
📣 **Channel:** {x["uploader"]}
🔗 **Link:** {x["webpage_url"]}

⚡️ __Powered by Hyper Robot__"""
            link = (x["webpage_url"])
            buttons = personal_markup(link)
            userid = message.from_user.id
            thumb = await down_thumb(thumbnail, userid)
            await app.send_photo(message.chat.id,
                photo=thumb,                 
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if str(finxx) == "sud":
            sudoers = await get_sudoers()
            text = "**💡 Sudo Users List:**\n\n"
            for count, user_id in enumerate(sudoers, 1):
                try:                     
                    user = await app.get_users(user_id)
                    user = user.first_name if not user.mention else user.mention
                except Exception:
                    continue                     
                text += f"➤ {user}\n"
            if not text:
                await message.reply_text("❌ no sudo users found")  
            else:
                await message.reply_text(text)
