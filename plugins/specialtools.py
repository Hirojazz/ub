# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}wspr <username>`
    Send secret message..

• `{i}sticker <query>`
    Search Stickers as Per ur Wish..

• `{i}getaudio <reply to an audio>`
    Download Audio To put in ur Desired Video/Gif.

• `{i}addaudio <reply to Video/gif>`
    It will put the above audio to the replied video/gif.

• `{i}dob <date of birth>`
    Put in dd/mm/yy Format only(eg .dob 01/01/1999).

• `{i}wall <query>`
    Search Hd Wallpaper as Per ur Wish..
"""
import os
import time
from datetime import datetime as dt
from random import choice
from shutil import rmtree

import moviepy.editor as m
import pytz
import requests
from bs4 import BeautifulSoup as bs
from pyUltroid.functions.google_image import googleimagesdownload
from pyUltroid.functions.tools import metadata
from telethon.tl.types import DocumentAttributeVideo

from . import *


@ultroid_cmd(
    pattern="getaudio$",
)
async def daudtoid(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await eor(event, "`Reply To Audio Only..`")
        return
    xx = await eor(event, "`processing...`")
    d = os.path.join("resources/extras/", "ul.mp3")
    await xx.edit("`Downloading... Large Files Takes Time..`")
    await event.client.download_media(ureply, d)
    await xx.edit("`Done.. Now reply to video In which u want to add that Audio`")


@ultroid_cmd(
    pattern="addaudio$",
)
async def adaudroid(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await eor(event, "`Reply To Gif/Video In which u want to add audio.`")
        return
    xx = await eor(event, "`processing...`")
    ultt = await ureply.download_media()
    ls = os.listdir("resources/extras")
    z = "ul.mp3"
    x = "resources/extras/ul.mp3"
    if z not in ls:
        await xx.edit("`First reply an audio with .aw`")
        return
    video = m.VideoFileClip(ultt)
    audio = m.AudioFileClip(x)
    out = video.set_audio(audio)
    out.write_videofile("ok.mp4", fps=30)
    await event.client.send_file(
        event.chat_id,
        file="ok.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xxx.delete()
    os.remove(out)
    os.remove(file.name)
    File.clear()
    os.remove(File[0])


@ultroid_cmd(
    pattern=r"dob ?(.*)",
)
async def hbd(event):
    if not event.pattern_match.group(1):
        return await eor(event, get_string("spcltool_6"))
    if event.reply_to_msg_id:
        kk = await event.get_reply_message()
        nam = await event.client.get_entity(kk.from_id)
        name = nam.first_name
    else:
        name = ultroid_bot.me.first_name
    zn = pytz.timezone("Asia/Kolkata")
    abhi = dt.now(zn)
    n = event.text
    q = n[5:]
    kk = q.split("/")
    p = kk[0]
    r = kk[1]
    s = kk[2]
    day = int(p)
    month = r
    paida = q
    try:
        jn = dt.strptime(paida, "%d/%m/%Y")
    except BaseException:
        return await eor(event, get_string("spcltool_6"))
    jnm = zn.localize(jn)
    zinda = abhi - jnm
    barsh = (zinda.total_seconds()) / (365.242 * 24 * 3600)
    saal = int(barsh)
    mash = (barsh - saal) * 12
    mahina = int(mash)
    divas = (mash - mahina) * (365.242 / 12)
    din = int(divas)
    samay = (divas - din) * 24
    ghanta = int(samay)
    pehl = (samay - ghanta) * 60
    mi = int(pehl)
    sec = (pehl - mi) * 60
    slive = int(sec)
    y = int(s) + int(saal) + 1
    m = int(r)
    brth = dt(y, m, day)
    cm = dt(abhi.year, brth.month, brth.day)
    ish = (cm - abhi.today()).days + 1
    dan = ish
    if dan == 0:
        hp = "`Happy BirthDay To U🎉🎊`"
    elif dan < 0:
        okk = 365 + ish
        hp = f"{okk} Days Left 🥳"
    elif dan > 0:
        hp = f"{ish} Days Left 🥳"
    if month == "12":
        sign = "Sagittarius" if (day < 22) else "Capricorn"
    elif month == "01":
        sign = "Capricorn" if (day < 20) else "Aquarius"
    elif month == "02":
        sign = "Aquarius" if (day < 19) else "Pisces"
    elif month == "03":
        sign = "Pisces" if (day < 21) else "Aries"
    elif month == "04":
        sign = "Aries" if (day < 20) else "Taurus"
    elif month == "05":
        sign = "Taurus" if (day < 21) else "Gemini"
    elif month == "06":
        sign = "Gemini" if (day < 21) else "Cancer"
    elif month == "07":
        sign = "Cancer" if (day < 23) else "Leo"
    elif month == "08":
        sign = "Leo" if (day < 23) else "Virgo"
    elif month == "09":
        sign = "Virgo" if (day < 23) else "Libra"
    elif month == "10":
        sign = "Libra" if (day < 23) else "Scorpion"
    elif month == "11":
        sign = "Scorpio" if (day < 22) else "Sagittarius"
    sign = f"{sign}"
    params = (("sign", sign), ("today", day))
    json = await async_searcher(
        "https://aztro.sameerkumar.website/", post=True, params=params, re_json=True
    )
    dd = json.get("current_date")
    ds = json.get("description")
    lt = json.get("lucky_time")
    md = json.get("mood")
    cl = json.get("color")
    ln = json.get("lucky_number")
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"""
    Name -: {name}

D.O.B -:  {paida}

Lived -:  {saal}yr, {mahina}m, {din}d, {ghanta}hr, {mi}min, {slive}sec

Birthday -: {hp}

Zodiac -: {sign}

**Horoscope On {dd} -**

`{ds}`

    Lucky Time :-        {lt}
    Lucky Number :-   {ln}
    Lucky Color :-        {cl}
    Mood :-                   {md}
    """,
        reply_to=event.reply_to_msg_id,
    )


@ultroid_cmd(pattern="sticker ?(.*)")
async def _(event):
    x = event.pattern_match.group(1)
    if not x:
        return await eor(event, "`Give something to search`")
    uu = await eor(event, get_string("com_1"))
    z = bs(
        await async_searcher("https://combot.org/telegram/stickers?q=" + x),
        "html.parser",
    )
    packs = z.find_all("div", "sticker-pack__header")
    sticks = {
        c.a["href"]: c.find("div", {"class": "sticker-pack__title"}).text for c in packs
    }

    if not sticks:
        return await uu.edit(get_string("spcltool_9"))
    a = "SᴛɪᴄᴋEʀs Aᴠᴀɪʟᴀʙʟᴇ ~\n\n"
    for _, value in sticks.items():
        a += f"<a href={_}>{value}</a>\n"
    await uu.edit(a, parse_mode="html")


@ultroid_cmd(pattern="wall ?(.*)")
async def wall(event):
    inp = event.pattern_match.group(1)
    if not inp:
        return await eor(event, "`Give me something to search..`")
    nn = await eor(event, get_string("com_1"))
    query = f"hd {inp}"
    gi = googleimagesdownload()
    args = {
        "keywords": query,
        "limit": 10,
        "format": "jpg",
        "output_directory": "./resources/downloads/",
    }
    gi.download(args)
    xx = choice(os.listdir(os.path.abspath(f"./resources/downloads/{query}/")))
    await event.client.send_file(event.chat_id, f"./resources/downloads/{query}/{xx}")
    rmtree(f"./resources/downloads/{query}/")
    await nn.delete()

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
