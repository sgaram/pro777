# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from threading import Thread
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit
import subprocess
import timeit

sc1 = LINE("EzD2VtmJZqSQuxSYULCc.Uv/0YYcEoAwu5rWj4Sx9Ja.KtwDgO6+EDMv4I9Bj7OFteu7v2yJ4bSXlubAJ6LQkVw=") #Akun Utama
sc1Mid = sc1.profile.mid
sc1Profile = sc1.getProfile()
sc1Settings = sc1.getSettings()
sc1Poll = OEPoll(sc1)
botStart = time.time()

cl = LINE("EzqxUlHa7fJ4CK6nW2Af.XzmbAwonn5keEY4vw/uKlW.gnHUb4aVq0LJzAvMilB/sugwliFTEMHOrIDaibzLnXc=") 
clMid = cl.profile.mid
clProfile = cl.getProfile()
clSettings = cl.getSettings()
clPoll = OEPoll(cl)
botStart = time.time()

ki = LINE("EzqfkU8n35nOkRW0tGf0.9T/PGPFdadrWbCl3Gzx/Ga.t6314tHfihMLXerKkc88/Z9D22vxibAI7fbMi5A6VZ0=")
kiMid = ki.profile.mid
kiProfile = ki.getProfile()
kiSettings = ki.getSettings()
kiPoll = OEPoll(ki)
botStart = time.time()

kk = LINE("EzwkQRV4ikVFeHlbZFYd.tLlReCirgG96uB+Q5pwO+q.T05h54NBMRTj44/an2PUZ53WvWA4EINswnGhb7GNuZA=")
kkMid = kk.profile.mid
kkProfile = kk.getProfile()
kkSettings = kk.getSettings()
kkPoll = OEPoll(kk)
botStart = time.time()

kc = LINE("Ezx1c4NT2uh6K9ET9191.lXZ4ob/KwrCUJfHRJ603qq.T2l+rfV80gtnFaUpLCHPD9Zft8QBagBPIIRmyj/g6X8=")
kcMid = kc.profile.mid
kcProfile = kc.getProfile()
kcSettings = kc.getSettings()
kcPoll = OEPoll(kc)
botStart = time.time()

responsename = sc1.getProfile().displayName
responsename1 = cl.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = kk.getProfile().displayName
responsename4 = kc.getProfile().displayName


msg_dict = {}

KAC = [sc1,cl,ki,kk,kc]
sc1MID = sc1.profile.mid
clMID = cl.profile.mid
kiMID = ki.profile.mid
kkMID = kk.profile.mid
kcMID = kc.profile.mid

Bots = [sc1,cl,kiMID,kkMID,kcMID]
creator = ["u9f09cfcb17d037e2936b751bd9d40ead"]
Owner = ["u9f09cfcb17d037e2936b751bd9d40ead"]
admin = ["u9f09cfcb17d037e2936b751bd9d40ead"]

settings = {
    "wblack": False,
    "dblack": False,
    "blacklist": {},
    "wblacklist": False,
    "dblacklist": False,
    "autoAdd": True,
    "inviteprotect": False,
    "protect": False,
    "qrprotect": False,
    "cancelprotect": False,
    "Wc": False,
    "limit": 50,
    "limits": 50,
    "lang":"JP",
    "autoJoin": True,
    "selfbot":True,
    "autoLeave": True,
    "autoRead": False,
    "autoRespon": False,
    "responMention": False,
    "autoJoinTicket": False,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": ".",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": False
}
wait = {
    'autoAdd': False,
    "tagme":"Tag detect",
    "autoRespon": False,
    "detectMention": False,
    "pname": False,
    "winvite": False,
    "qr": False,
    "Lv": False,
    "lang":"JP",
    "pro_name":{},
    "unsend": True,
    "Addsticker":{
            "name": "",
            "status":False
            },
    'message':"""Thanks For Add Me
Bot Public By sepri_che
Contact Me : https://line.me/ti/p/sepriche""",
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{}
}


try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

setTime = {}
setTime = read['readTime']
   
settings["myProfile"]["displayName"] = sc1Profile.displayName
settings["myProfile"]["statusMessage"] = sc1Profile.statusMessage
settings["myProfile"]["pictureStatus"] = sc1Profile.pictureStatus
coverId = sc1.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def logError(text):
    sc1.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                sc1.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@sc1bot "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    sc1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider Userã€Œ{}ã€\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâ•šâ•â•[ {} ]".format(str(sc1.getGroup(to).name))
                except:
                    no = "\nâ•šâ•â•[ Success ]"
        sc1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sc1.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessage =   "╭════════╬╬════════╮" + "\n" + \
                    "       sᴇᴘʀɪ ʙᴏᴛ " + "\n" + \
                    "╰════════╬╬════════╯" + "\n" \
                    "╭☞[ Protect Command ]" + "\n" + \
                    "╠☞ " + key + "Protect 「On/Off」" + "\n" + \
                    "╠☞ " + key + "QrProtect 「On/Off」" + "\n" + \
                    "╠☞ " + key + "InvProtect 「On/Off」" + "\n" + \
                    "╠☞ " + key + "CancelProtect 「On/Off」" + "\n" + \
                    "╠☞ " + key + "SetPro 「On/Off」" + "\n" + \
                    "╠☞ " + key + "sc1 Masuk" + "\n" + \
                    "╠☞ " + key + "sc1 Out" + "\n" + \
                    "╠══[ Staff Add/Del Command ]" + "\n" + \
                    "║☞ " + key + "Staff add 「Mention」" + "\n" + \
                    "║☞ " + key + "Staff del 「Mention」" + "\n" + \
                    "╠══[ Default Command ]" + "\n" + \
                    "║☞ " + key + "Creator" + "\n" + \
                    "║☞ " + key + "Speed" + "\n" + \
                    "║☞ " + key + "Runtime" + "\n" + \
                    "║☞ " + key + "Status" + "\n" + \
                    "║☞ " + key + "Respon" + "\n" + \
                    "║☞ " + key + "About" + "\n" + \
                    "╠══[ Daftar Admin Bot ]" + "\n" + \
                    "║☞ " + key + "Ownerlist" + "\n" + \
                    "╰☞ " + key + "Stafflist" + "\n" + \
                    "╭════════╬╬════════╮" + "\n" + \
                    "       sᴇᴘʀɪ ʙᴏᴛ" + "\n" + \
                    "╰════════╬╬════════╯"
    return helpMessage

def clientBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            if wait["autoAdd"] == True:
                sc1.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    sc1.sendMessage(op.param1,str(wait["message"]))

        if op.type == 5:
            print ("INFO SELBOT : ADA YANG ADD")
            if settings["autoAdd"] == True:
                sc1.sendMessage(op.param1, "Thanks For Add Me")

        if op.type == 19:
                if op.param2 not in Bots:
                    if op.param2 not in Owner + admin:
                            pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)

        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 not in Owner + admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Owner + admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        sc1.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        sc1.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        sc1.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        sc1.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        sc1.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        sc1.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        sc1.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        sc1.sendMessage(msg.to,"Done")

        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 not in Owner + admin + Bots:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = sc1.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    Ticket = sc1.reissueGroupTicket(op.param1)
                    sc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G = sc1.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    sc1.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    sc1.updateGroup(G)
                else:
                    sc1.sendMessage(op.param1,"Dont Play QR This Already Protect")
            else:
                sc1.sendMessage(op.param1,"")

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if sc1Mid in op.param3:
                if settings["autoJoin"] == True:
                    sc1.acceptGroupInvitation(op.param1)

        if op.type == 13:
            print ("INFO SELBOT : ADA YANG INVITE GRUP")
            group = sc1.getGroup(op.param1)
            if settings["autoJoin"] == True:
                sc1.acceptGroupInvitation(op.param1)

        if op.type == 17:
            print ("MEMBER HAS JOIN THE GROUP")
            if settings["autoJoin"] == True:
               ginfo = sc1.getGroup(op.param1)

        if op.type == 19:
            if Bots in op.param3:
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                random.choice(KAC).acceptGroupInvitation(op.param1)

        if op.type == 19:
            if op.param3 in admin + Owner + Bots:
              if op.param2 in Bots:
                pass
              if op.param2 in admin + Bots + Owner:
                pass
              else:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  random.choice(KAC).acceptGroupInvitation(op.param1)

        if op.type == 19:
            if op.param3 in Bots:
              if op.param2 in Bots:
                pass
              if op.param2 in Bots:
                pass
              else:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  random.choice(KAC).acceptGroupInvitation(op.param1)

            if op.param3 in kiMID:
                G = ki.getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                sc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.1)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                sc1.updateGroup(G)
            if op.param3 in sc1Mid + kiMID + kkMID + kcMID:
                G = random.choice(KAC).getGroup(msg.to)
                ginfo = random.choice(KAC).getGroup(msg.to)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                invsend = 0
                Ticket = random.choice(KAC).reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                G = random.choice(KAC).getGroup(msg.to)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                G.preventedJoinByTicket(G)
                random.choice(KAC).updateGroup(G)

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = kk.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 kk.sendMessage(msg.to,"-> " + _name + " was here")
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     kk.findAndAddContactsByMid(target)
                                     kk.inviteIntoGroup(msg.to,[target])
                                     kk.sendMessage(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         kk.findAndAddContactsByMid(invite)
                                         kk.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         kk.sendMessage(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break

        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != sc1.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                sc1.sendMessage(to, str(helpMessage))
                            if cmd == "oa ecchi":
                                sc1.sendMessage(to,"ᴛᴇᴀᴍ ʜᴀᴄᴋʙᴏᴛ ʀᴇsɪᴅɪᴠɪs ᴋɪʟʟᴇʀ")
                                sc1.sendContact(to,"u9f09cfcb17d037e2936b751bd9d40ead")
                            if cmd == "creator":
                                sc1.sendMessage(to,"")
                                sc1.sendContact(to,"u9f09cfcb17d037e2936b751bd9d40ead")
                            elif cmd == "speed":
                                start = time.time()
                                sc1.sendMessage(to, "ᴄʜᴇᴄᴋ sᴘᴇᴇᴅ sᴇᴘʀɪʙᴏᴛ...")
                                elapsed_time = time.time() - start
                                sc1.sendMessage(to, "[ Speed ]\n{} seconds".format(str(elapsed_time)))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                sc1.sendMessage(to, "sᴇᴘʀɪ ʙᴏᴛ Has Been Run {}".format(str(runtime)))
                            elif cmd == 'about':
                                try:
                                    arr = []
                                    owner = "u9f09cfcb17d037e2936b751bd9d40ead"
                                    creator = sc1.getContact(owner)
                                    contact = sc1.getContact(sc1MID)
                                    grouplist = sc1.getGroupIdsJoined()
                                    contactlist = sc1.getAllContactIds()
                                    blockedlist = sc1.getBlockedContactIds()
                                    ret_ = "╔══[ sᴇᴘʀɪ ʙᴏᴛ ]"
                                    ret_ += "\n╠ Name : {}".format(contact.displayName)
                                    ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                                    ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                                    ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                                    ret_ += "\n╠══[ sᴇᴘʀɪ ʙᴏᴛ ]"
                                    ret_ += "\n╠ Version : Premium"
                                    ret_ += "\n╠ Creator : {}".format(creator.displayName)
                                    ret_ += "\n╚══[ sᴇᴘʀɪ ʙᴏᴛ ]"
                                    sc1.sendMessage(msg.to, "Special Thanks To\n\n-Author LinePy\n-HelloWorld\n-Bot Eater\n-NadyaTj\n-All My Friends")
                                    sc1.sendMessage(to, str(ret_))
                                except Exception as e:
                                    sc1.sendMessage(msg.to, str(e))
#----------------------------Status Command---------------------#
                            elif cmd == "autoadd on":
                                if msg._from in Owner:
                                    settings["autoAdd"] = True
                                    sc1.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                                if msg._from in Owner:
                                    settings["autoAdd"] = False
                                    sc1.sendMessage(to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                                if msg._from in Owner:
                                    settings["autoJoin"] = True
                                    sc1.sendMessage(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                                if msg._from in Owner:
                                    settings["autoJoin"] = False
                                    sc1.sendMessage(to, "Berhasil menonaktifkan auto join")
                            elif cmd == "status":
                                try:
                                    ret_ = "╔══[ Status ]"
                                    if settings["protect"] == True: ret_ += "\n╠══[ ON ] Protect"
                                    else: ret_ += "\n╠══[ OFF ] Protect"
                                    if settings["qrprotect"] == True: ret_ += "\n╠══[ ON ] Qr Protect"
                                    else: ret_ += "\n╠══[ OFF ] Qr Protect"
                                    if settings["inviteprotect"] == True: ret_ += "\n╠══[ ON ] Invite Protect"
                                    else: ret_ += "\n╠══[ OFF ] Invite Protect"
                                    if settings["cancelprotect"] == True: ret_ += "\n╠══[ ON ] Cancel Protect"
                                    else: ret_ += "\n╠══[ OFF ] Cancel Protect"
                                    if settings["autoJoin"] == True: ret_ += "\n╠══[ ON ] Auto Join"
                                    else: ret_ += "\n╠══[ OFF ] Auto Join"
                                    ret_ += "\n╚══[ sᴇᴘʀɪ ʙᴏᴛ ]"
                                    sc1.sendMessage(to, str(ret_))
                                except Exception as e:
                                    sc1.sendMessage(msg.to, str(e))
#----------------------------------Staff Add,Del Command-------------------------------#
                            elif "Staff add @" in msg.text:
                                if msg._from in Owners:
                                    print ("[Command]Staff add executing")
                                    _name = msg.text.replace("Staff add @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = sc1.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = kk.getGroup(msg.to)
                                    gs = kc.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            sc1.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                admin.append(target)
                                                sc1.sendMessage(msg.to,"Staff Ditambahkan")
                                            except:
                                                pass
                                    print ("[Command]Staff add executed")
                                else:
                                    sc1.sendMessage(msg.to,"Command denied.")
                                    sc1.sendMessage(msg.to,"Creator permission required.")
                            elif "Staff del @" in msg.text:
                                if msg._from in Owners:
                                    print ("[Command]Staff remove executing")
                                    _name = msg.text.replace("Staff del @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = sc1.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = kk.getGroup(msg.to)
                                    gs = kc.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            sc1.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                admin.remove(target)
                                                sc1.sendMessage(msg.to,"Staff Dihapus")
                                            except:
                                                pass
                                    print ("[Command]Staff remove executed")
                                else:
                                    sc1.sendMessage(msg.to,"Command denied.")
                                    sc1.sendMessage(msg.to,"Creator permission required.")
#--------------------------Change Name Command---------------------------#
                            elif cmd.startswith("sc1:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = sc1.getProfile()
                                    profile.displayName = string
                                    sc1.updateProfile(profile)
                                    sc1.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("cl:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ki.getProfile()
                                    profile.displayName = string
                                    ki.updateProfile(profile)
                                    ki.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("sc12:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = kk.getProfile()
                                    profile.displayName = string
                                    kk.updateProfile(profile)
                                    kk.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("sc13:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = kc.getProfile()
                                    profile.displayName = string
                                    kc.updateProfile(profile)
                                    kc.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
#----------------------------------Change Bio Command-------------------------------#
                            elif cmd.startswith("sc1bio:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = sc1.getProfile()
                                    profile.statusMessage = string
                                    sc1.updateProfile(profile)
                                    sc1.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("sc1bio1:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ki.getProfile()
                                    profile.statusMessage = string
                                    ki.updateProfile(profile)
                                    ki.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("sc1bio2:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = kk.getProfile()
                                    profile.statusMessage = string
                                    kk.updateProfile(profile)
                                    kk.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("sc1bio3:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = kc.getProfile()
                                    profile.statusMessage = string
                                    kc.updateProfile(profile)
                                    kc.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
#------------------------------Respon Command--------------------------#
                            elif text.lower() == "respon":
                                    sc1.sendMessage(msg.to, "sTay")
                                    ki.sendMessage(msg.to, "sTay")
                                    kk.sendMessage(msg.to, "sTay")
                                    kc.sendMessage(msg.to, "sTy")
                                    cl.sendMessage(msg.to, "sTay")
                            elif text.lower() == 'clearban':
                                if msg._from in Owner:
                                    settings["blacklist"] = {}
                                    sc1.sendMessage(msg.to,"Blacklist Dibersihkan")
#------------------------------Join Command---------------------------#
                            elif text.lower() in ["masuk"]:
                                if msg._from in Owner:    
                                    G = sc1.getGroup(msg.to)
                                    ginfo = sc1.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    sc1.updateGroup(G)
                                    invsend = 0
                                    Ticket = sc1.reissueGroupTicket(msg.to)
                                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    G = sc1.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    sc1.updateGroup(G)
                                    G.preventedJoinByTicket(G)
                                    sc1.updateGroup(G)
                            elif text.lower() in ["byeall"]:
                                if msg._from in Owner:   								
                                    ki.leaveGroup(msg.to)
                                    kk.leaveGroup(msg.to)
                                    kc.leaveGroup(msg.to)
                                    cl.leaveGroup(msg.to)	
#-------------------------------Protect Command-------------------------------#
                            elif text.lower() == 'protect on':
                                if msg._from in admin and Owner:
                                        if settings["protect"] == True:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Already On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Set To On")
                                        else:
                                            settings["protect"] = True
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Set To On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Already On")
                            elif text.lower() == 'protect off':
                                if msg._from in admin and Owner:
                                        if settings["protect"] == False:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Already Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Set To Off")
                                        else:
                                            settings["protect"] = False
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Set To Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Already Off")
                            elif text.lower() == 'qrprotect on':
                                if msg._from in admin and Owner:
                                        if settings["qrprotect"] == True:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection QR Already On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection QR Set To On")
                                        else:
                                            settings["qrprotect"] = True
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection QR Set To On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection QR Already On")
                            elif text.lower() == 'cancelprotect on':
                                if msg._from in admin and Owner:
                                        if settings["cancelprotect"] == True:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Already On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Set To On")
                                        else:
                                            settings["cancelprotect"] = True
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Set To On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Already On")
                            elif text.lower() == 'cancelprotect off':
                                if msg._from in admin and Owner:
                                        if settings["cancelprotect"] == False:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Already Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Set To Off")
                                        else:
                                            settings["cancelprotect"] = False
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Set To Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Cancel Already Off")
                            elif text.lower() == 'invprotect on':
                                if msg._from in admin and Owner:
                                        if settings["inviteprotect"] == True:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Already On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Set To On")
                                        else:
                                            settings["inviteprotect"] = True
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Set To On")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Already On")
                            elif text.lower() == 'invprotect off':
                                if msg._from in admin and Owner:
                                        if settings["inviteprotect"] == False:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Already Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                                        else:
                                            settings["inviteprotect"] = False
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection Invite Already Off")
                            elif text.lower() == 'qrprotect off':
                                if msg._from in admin and Owner:
                                        if settings["qrprotect"] == False:
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection QR Already Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection QR Set To Off")
                                        else:
                                            settings["qrprotect"] = False
                                            if settings["lang"] == "JP":
                                                sc1.sendMessage(msg.to,"➲ Protection QR Set To Off")
                                            else:
                                                sc1.sendMessage(msg.to,"➲ Protection QR Already Off")
                            elif text.lower() == 'setpro on':
                                if msg._from in Owner + admin:
                                    settings["protect"] = True
                                    settings["qrprotect"] = True
                                    settings["inviteprotect"] = True
                                    settings["cancelprotect"] = True
                                    sc1.sendMessage(msg.to," All Protection Set To On")
                                else:
                                    sc1.sendMessage(msg.to,"Just for Owner")
                            elif text.lower() == 'setpro off':
                                if msg._from in Owner + admin:
                                    settings["protect"] = False
                                    settings["qrprotect"] = False
                                    settings["inviteprotect"] = False
                                    settings["cancelprotect"] = False
                                    sc1.sendMessage(msg.to," All Protect Set To Off")
                                else:
                                    sc1.sendMessage(msg.to,"Just for Owner")
#------------------------------Owner , Staff List------------------------------#
                            elif msg.text in ["Ownerlist","ownerlist"]:
                                if Owner == []:
                                    sc1.sendMessage(msg.to,"The Ownerlist is empty")
                                else:
                                    sc1.sendMessage(msg.to,"Tunggu...")
                                    mc = ""
                                    mc = "╔══[ Owner Bot Protect ]"
                                    for mi_d in Owner:
                                        mc += "\n╠ "+sc1.getContact(mi_d).displayName + "\n"
                                    mc += "╚══[ Finish ]"
                                    sc1.sendMessage(msg.to,mc)
                            elif msg.text in ["Stafflist","stafflist"]:
                                if admin == []:
                                    sc1.sendMessage(msg.to,"The stafflist is empty")
                                else:
                                    sc1.sendMessage(msg.to,"Tunggu...")
                                    mc = ""
                                    mc = "╔══[ Staff Bot Protect ]"
                                    for mi_d in admin:
                                        mc += "\n╠ "+sc1.getContact(mi_d).displayName + "\n"
                                    mc += "╚══[ Finish ]"
                                    sc1.sendMessage(msg.to,mc)
#------------------------------Owner Add , Del---------------------------------#
                            elif "Owner add @" in msg.text:
                                if msg._from in Owner:
                                    print ("[Command]Owner add executing")
                                    _name = msg.text.replace("Owner add @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = sc1.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = kk.getGroup(msg.to)
                                    gs = kc.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            sc1.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                Owner.append(target)
                                                sc1.sendMessage(msg.to,"Owner Ditambahkan")
                                            except:
                                                pass
                                    print ("[Command]Owner add executed")
                                else:
                                    sc1.sendMessage(msg.to,"Command denied.")
                                    sc1.sendMessage(msg.to,"Owner permission required.")
                            elif "Owner del @" in msg.text:
                                if msg._from in Owner:
                                    print ("[Command]Owner del executing")
                                    _name = msg.text.replace("Owner del @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = sc1.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = kk.getGroup(msg.to)
                                    gs = kc.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            sc1.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                Owner.remove(target)
                                                sc1.sendMessage(msg.to,"Owner Dihapus")
                                            except:
                                                pass
                                    print ("[Command]Owner del executed")
                                else:
                                    sc1.sendMessage(msg.to,"Command denied.")
                                    sc1.sendMessage(msg.to,"Owner permission required.")
#------------------------------Pembatas Script---------------------------------#
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = sc1.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            sc1.updateProfilePicture(path)
                            sc1.sendMessage(to, "Berhasil mengubah foto profile")
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = ki.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            ki.updateProfilePicture(path)
                            ki.sendMessage(to, "Berhasil mengubah foto profile")
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = kk.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            kk.updateProfilePicture(path)
                            kc.sendMessage(to, "Berhasil mengubah foto profile")
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = kc.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            kc.updateProfilePicture(path)
                            kc.sendMessage(to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = sc1.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                sc1.updateGroupPicture(to, path)
                                sc1.sendMessage(to, "Berhasil mengubah foto group")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔══[ Sticker Info ]"
                            ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                            ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚══[ Finish ]"
                            sc1.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = sc1.getContact(msg.contentMetadata["mid"])
                                if sc1 != None:
                                    cover = sc1.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    sc1.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔══[ Details Contact ]"
                                ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╚══[ Finish ]"
                                sc1.sendMessage(to, str(ret_))
                            except:
                                sc1.sendMessage(to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = sc1.getContact(sender)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                sc1.sendMessage(to, str(ret_))
                            except:
                                sc1.sendMessage(to, "🙄🙄🙄")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != sc1.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        sc1.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            sc1.sendMessage(msg.to,text)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                sc1.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                sc1.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = sc1.findGroupByTicket(ticket_id)
                                    sc1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    sc1.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))

                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if sc1Mid in mention["M"]:
                                        if settings["autoRespon"] == True:
                                            sendMention(sender, "Oit @!,hadir", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)


        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
           
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass               
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = sc1Poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                sc1Poll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
