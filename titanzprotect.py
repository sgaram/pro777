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

#Done Fixed Bots Reinvite Owner,Admin,Assist

#Penambahan 1 Assist

 #---------------------------------Please Dont Edit The Creator-----------------------------#
 #                  					Titanz Bot Protect									#
 #                 Tolong Hargai Creator Bot Ini 											#
 #                                              Jangan Edit Creator Nya :"(					#
 #                 Jangan Sombong Memakai Bot Orang 										#
 #                                              Ini Bot Free , Not For Sale					#
 #			       Creator Titanz Bot : Ferianss / https://line.me/ti/p/YFBy7TqfVg			#
 #                       Chat Creator Titanz Bot Jika Mengalami Error 						#
 #------------------------------------------------------------------------------------------#

titanz = LINE("EvTS2oby6YPMbuWGsZb8.yAM1ZO3J61gOwuemMdtLYa.NYpAUwfsDoveZRrvB2RGI0vloyo5OzqkByoMLfRi9lg=") #Akun Utama
titanzMid = titanz.profile.mid
titanzProfile = titanz.getProfile()
titanzSettings = titanz.getSettings()
titanzPoll = OEPoll(titanz)
botStart = time.time()

titanz1 = LINE("EvEVQLO78i9hFFODKTK7.rYQ2taYWmIaHwZoX6iKQ1W.exfNW1KWDc2oV/QLDefJqPXRHZ0TnmXc+Vp9V29uQME=") #Akun Khusus Reinvite Owner atau Assist
titanz1Mid = titanz1.profile.mid
titanz1Profile = titanz1.getProfile()
titanz1Settings = titanz1.getSettings()
titanz1Poll = OEPoll(titanz1)
botStart = time.time()

ki = LINE("Evy7OCsYZ8chr5NMYgy6.BaiKNxR2VN7zWCBrQS6P5G.jl5NAyvvW9894OTD1Bk9U7gvYb/gc2WaypEAApxO36Q=") #Assist 1
kiMid = ki.profile.mid
kiProfile = ki.getProfile()
kiSettings = ki.getSettings()
kiPoll = OEPoll(ki)
botStart = time.time()

ki2 = LINE("Evu5s0D5n8nlvLrt84Ca.UHbbg4pHBjT5VwCYtXmXsG.AY3zejVR4B7uEU9kYp17X3+UG3koCdUS9SCslWdAoZA=") #Assist 2
ki2Mid = ki2.profile.mid
ki2Profile = ki2.getProfile()
ki2Settings = ki2.getSettings()
ki2Poll = OEPoll(ki2)
botStart = time.time()

ki3 = LINE("EvEk09kUJvUTXAUZNZWa.Oyj1ZAWaMt3CKaVDd5BW2G.0MUkEP4BZLuACIpJOn+KWtykglPbGlE5x5DCg+ZH0PA=") #Assist 3
ki3Mid = ki3.profile.mid
ki3Profile = ki3.getProfile()
ki3Settings = ki3.getSettings()
ki3Poll = OEPoll(ki3)
botStart = time.time()

ki4 = LINE("EvE5gN5SQWYezKPqieLf.K9hUseF6j4f/WE5DLTHHBW.fmW4IX9Geq6Pd17J4siBRvxrTuq18Znv12p84xS/mqc=") #Assist 4
ki4Mid = ki4.profile.mid
ki4Profile = ki4.getProfile()
ki4Settings = ki4.getSettings()
ki4Poll = OEPoll(ki4)
botStart = time.time()

ki5 = LINE("Evi2vObUZ3IgPfAr7b7f.eb8Fsy+dW4odT30yu3UjtW.5nMPYL3L5QFU6CStG8/WfNDT4KWM9mEJbgwA1LT0Pfo=") #Bot Kick Luar (Ghost)
ki5Mid = ki5.profile.mid
ki5Profile = ki5.getProfile()
ki5Settings = ki5.getSettings()
ki5Poll = OEPoll(ki5)
botStart = time.time()

responsename = titanz.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = ki2.getProfile().displayName
responsename4 = ki3.getProfile().displayName
responsename5 = ki4.getProfile().displayName
responsename6 = ki5.getProfile().displayName


msg_dict = {}

KAC = [titanz,titanz1,ki,ki2,ki3,ki4]
titanzMID = titanz.profile.mid
titanz1MID = titanz1.profile.mid
kiMID = ki.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
ki4MID = ki4.profile.mid
ki5MID = ki5.profile.mid

#TAMBAHIN MID KAMU AJA 
#JANGAN DIHAPUS MID INI NGENTOD
Bots = [titanz,titanz1,kiMID,ki2MID,ki3MID,ki4MID,ki5MID]
creator = ["u61a9b5ce8de3eb51a859410c9834e5c8","u9f09cfcb17d037e2936b751bd9d40ead"]
Owner = ["u61a9b5ce8de3eb51a859410c9834e5c8","u9f09cfcb17d037e2936b751bd9d40ead","ud09e25c0ca9489be645b4afb00c27ee4","u3ba3da3a783bfd317d37f0d5f4ac20a2","uad49d6940b08ddae2a506e5a822c2aae","u4dea393659914ff968fab78963a6495d","u970bb76e49958f3d9e980e3a8e6ac36a","uc5676bcfe5b7409487dc9b129dd17909","u81196d0a27964b33b2123cfe165d7b36","uea36cc53121bef94d1e01ccc5dd29018","u91bb57b10dabe43801a6fffe8ad89340",]
admin = ["u61a9b5ce8de3eb51a859410c9834e5c8","u9f09cfcb17d037e2936b751bd9d40ead","ud09e25c0ca9489be645b4afb00c27ee4","u3ba3da3a783bfd317d37f0d5f4ac20a2","uad49d6940b08ddae2a506e5a822c2aae","u4dea393659914ff968fab78963a6495d","u970bb76e49958f3d9e980e3a8e6ac36a","uc5676bcfe5b7409487dc9b129dd17909","u81196d0a27964b33b2123cfe165d7b36","uea36cc53121bef94d1e01ccc5dd29018","u91bb57b10dabe43801a6fffe8ad89340",]

settings = {
    "wblack": False,
    "dblack": False,
    "blacklist": {},
    "wblacklist": False,
    "dblacklist": False,
    "autoAdd": True,
    "inviteprotect": True,
    "protect": True,
    "qrprotect": True,
    "cancelprotect": True,
    "Wc": True,
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
    "checkContact": True,
    "checkPost": True,
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
   
settings["myProfile"]["displayName"] = titanzProfile.displayName
settings["myProfile"]["statusMessage"] = titanzProfile.statusMessage
settings["myProfile"]["pictureStatus"] = titanzProfile.pictureStatus
coverId = titanz.getProfileDetail()["result"]["objectId"]
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
    titanz.log("[ ERROR ] {}".format(str(text)))
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
                titanz.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@titanzbot "
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
    titanz.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

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
                    no = "\nâ•šâ•â•[ {} ]".format(str(titanz.getGroup(to).name))
                except:
                    no = "\nâ•šâ•â•[ Success ]"
        titanz.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        titanz.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
                    "╠☞ " + key + "Titanz Masuk" + "\n" + \
                    "╠☞ " + key + "Titanz Out" + "\n" + \
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
                titanz.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    titanz.sendMessage(op.param1,str(wait["message"]))

        if op.type == 5:
            print ("INFO SELBOT : ADA YANG ADD")
            if settings["autoAdd"] == True:
                titanz.sendMessage(op.param1, "Thanks For Add Me {} \nBot By Inojin\nOwner : https://line.me/ti/p/YFBy7TqfVg".format(str(client.getContact(op.param1).displayName)))
        if op.type == 11:
            if op.param1 :
                try:
                    if titanz.getGroup(op.param1).preventedJoinByTicket == True:
                            clien.reissueGroupTicket(op.param1)
                            X = titanz.getGroup(op.param1)
                            titanz.updateGroup(X)
                except:
                    pass

        if op.type == 19:
                if op.param2 not in Bots:
                    if op.param2 in Owner + admin + Bots:
                            pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        G = titanz1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        titanz1.updateGroup(G)
                        invsend = 0
                        Ticket = titanz1.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.sendMessage(op.param1,"This Groups Has Been Protected!!")
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        titanz1.inviteIntoGroup(op.param1,[op.param3])
                        ki5.leaveGroup(op.param1)
                        random.choice(KAC).acceptGroupInvitation(op.param1)
                        G = titanz1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        titanz1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        titanz1.updateGroup(G)

        if op.type == 19:
                if op.param2 not in admin + Bots:
                    if op.param2 in Bots:
                            pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        G = titanz1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        titanz1.updateGroup(G)
                        invsend = 0
                        Ticket = titanz1.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.sendMessage(op.param1,"This Groups Has Been Protected!!")
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        titanz1.inviteIntoGroup(op.param1,[op.param3])
                        ki5.leaveGroup(op.param1)
                        random.choice(KAC).acceptGroupInvitation(op.param1)
                        G = titanz1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        titanz1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        titanz1.updateGroup(G)

        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Owner + admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    if op.param2 not in Bots:
                        if op.param2 in Owner + admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Owner + admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    if op.param2 not in Bots:
                        if op.param2 in Owner + admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        titanz.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        titanz.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        titanz.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        titanz.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        titanz.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        titanz.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        titanz.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        titanz.sendMessage(msg.to,"Done")

        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Owner + admin + Bots:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = titanz.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    Ticket = titanz.reissueGroupTicket(op.param1)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki5.kickoutFromGroup(op.param1,[op.param2])
                    ki5.leaveGroup(op.param1)
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(KAC).acceptGroupInvitation(op.param1)
                    G = titanz.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    titanz.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    titanz.updateGroup(G)
                else:
                    titanz.sendMessage(op.param1,"Dont Play QR This Already Protect")
            else:
                titanz.sendMessage(op.param1,"")

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if titanzMid in op.param3:
                if settings["autoJoin"] == True:
                    titanz.acceptGroupInvitation(op.param1)
                dan = titanz.getContact(op.param2)
                tgb = titanz.getGroup(op.param1)
                sendMention(op.param1, "Hallo @!, Thanks for invite me to your groups".format(str(tgb.name)),[op.param2])
                titanz.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                titanz.sendContact(op.param1, op.param2)

        if op.type == 13:
            print ("INFO SELBOT : ADA YANG INVITE GRUP")
            group = titanz.getGroup(op.param1)
            if settings["autoJoin"] == True:
                titanz.acceptGroupInvitation(op.param1)

        if op.type == 17:
            print ("MEMBER HAS JOIN THE GROUP")
            if settings["autoJoin"] == True:
               ginfo = titanz.getGroup(op.param1)

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
                titanz.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.1)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                titanz.updateGroup(G)
            if op.param3 in titanzMid + kiMID + ki2MID + ki3MID + ki4MID:
                G = random.choice(KAC).getGroup(msg.to)
                ginfo = random.choice(KAC).getGroup(msg.to)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                invsend = 0
                Ticket = random.choice(KAC).reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
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
                         groups = ki2.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki2.sendMessage(msg.to,"-> " + _name + " was here")
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki2.findAndAddContactsByMid(target)
                                     ki2.inviteIntoGroup(msg.to,[target])
                                     ki2.sendMessage(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki2.findAndAddContactsByMid(invite)
                                         ki2.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         ki2.sendMessage(msg.to,"Negative, Error detected")
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
                        if sender != titanz.profile.mid:
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
                                titanz.sendMessage(to, str(helpMessage))
                            if cmd == "oa ecchi":
                                titanz.sendMessage(to,"ᴛᴇᴀᴍ ʜᴀᴄᴋʙᴏᴛ ʀᴇsɪᴅɪᴠɪs ᴋɪʟʟᴇʀ")
                                titanz.sendContact(to,"u9f09cfcb17d037e2936b751bd9d40ead")
                            if cmd == "creator":
                                titanz.sendMessage(to,"")
                                titanz.sendContact(to,"u9f09cfcb17d037e2936b751bd9d40ead")
                            elif cmd == "speed":
                                start = time.time()
                                titanz.sendMessage(to, "ᴄʜᴇᴄᴋ sᴘᴇᴇᴅ sᴇᴘʀɪʙᴏᴛ...")
                                elapsed_time = time.time() - start
                                titanz.sendMessage(to, "[ Speed ]\n{} seconds".format(str(elapsed_time)))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                titanz.sendMessage(to, "sᴇᴘʀɪ ʙᴏᴛ Has Been Run {}".format(str(runtime)))
                            elif cmd == 'about':
                                try:
                                    arr = []
                                    owner = "u9f09cfcb17d037e2936b751bd9d40ead"
                                    creator = titanz.getContact(owner)
                                    contact = titanz.getContact(titanzMID)
                                    grouplist = titanz.getGroupIdsJoined()
                                    contactlist = titanz.getAllContactIds()
                                    blockedlist = titanz.getBlockedContactIds()
                                    ret_ = "╔══[ sᴇᴘʀɪ ʙᴏᴛ ]"
                                    ret_ += "\n╠ Name : {}".format(contact.displayName)
                                    ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                                    ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                                    ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                                    ret_ += "\n╠══[ sᴇᴘʀɪ ʙᴏᴛ ]"
                                    ret_ += "\n╠ Version : Premium"
                                    ret_ += "\n╠ Creator : {}".format(creator.displayName)
                                    ret_ += "\n╚══[ sᴇᴘʀɪ ʙᴏᴛ ]"
                                    titanz.sendMessage(msg.to, "Special Thanks To\n\n-Author LinePy\n-HelloWorld\n-Bot Eater\n-NadyaTj\n-All My Friends")
                                    titanz.sendMessage(to, str(ret_))
                                except Exception as e:
                                    titanz.sendMessage(msg.to, str(e))
#----------------------------Status Command---------------------#
                            elif cmd == "autoadd on":
                                if msg._from in Owner:
                                    settings["autoAdd"] = True
                                    titanz.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                                if msg._from in Owner:
                                    settings["autoAdd"] = False
                                    titanz.sendMessage(to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                                if msg._from in Owner:
                                    settings["autoJoin"] = True
                                    titanz.sendMessage(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                                if msg._from in Owner:
                                    settings["autoJoin"] = False
                                    titanz.sendMessage(to, "Berhasil menonaktifkan auto join")
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
                                    titanz.sendMessage(to, str(ret_))
                                except Exception as e:
                                    titanz.sendMessage(msg.to, str(e))
#----------------------------------Staff Add,Del Command-------------------------------#
                            elif "Staff add @" in msg.text:
                                if msg._from in Owners:
                                    print ("[Command]Staff add executing")
                                    _name = msg.text.replace("Staff add @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = titanz.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = ki2.getGroup(msg.to)
                                    gs = ki3.getGroup(msg.to)
                                    gs = ki4.getGroup(msg.to)
                                    gs = ki5.getGroup(msg.to)
                                    gs = titanz1.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            titanz.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                admin.append(target)
                                                titanz.sendMessage(msg.to,"Staff Ditambahkan")
                                            except:
                                                pass
                                    print ("[Command]Staff add executed")
                                else:
                                    titanz.sendMessage(msg.to,"Command denied.")
                                    titanz.sendMessage(msg.to,"Creator permission required.")
                            elif "Staff del @" in msg.text:
                                if msg._from in Owners:
                                    print ("[Command]Staff remove executing")
                                    _name = msg.text.replace("Staff del @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = titanz.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = ki2.getGroup(msg.to)
                                    gs = ki3.getGroup(msg.to)
                                    gs = ki4.getGroup(msg.to)
                                    gs = ki5.getGroup(msg.to)
                                    gs = titanz1.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            titanz.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                admin.remove(target)
                                                titanz.sendMessage(msg.to,"Staff Dihapus")
                                            except:
                                                pass
                                    print ("[Command]Staff remove executed")
                                else:
                                    titanz.sendMessage(msg.to,"Command denied.")
                                    titanz.sendMessage(msg.to,"Creator permission required.")
#--------------------------Change Name Command---------------------------#
                            elif cmd.startswith("titanz:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = titanz.getProfile()
                                    profile.displayName = string
                                    titanz.updateProfile(profile)
                                    titanz.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("titanz1:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ki.getProfile()
                                    profile.displayName = string
                                    ki.updateProfile(profile)
                                    ki.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("titanz2:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ki2.getProfile()
                                    profile.displayName = string
                                    ki2.updateProfile(profile)
                                    ki2.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("titanz3:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ki3.getProfile()
                                    profile.displayName = string
                                    ki3.updateProfile(profile)
                                    ki3.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("titanz4:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ki4.getProfile()
                                    profile.displayName = string
                                    ki4.updateProfile(profile)
                                    ki4.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("titanz5:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ki5.getProfile()
                                    profile.displayName = string
                                    ki5.updateProfile(profile)
                                    ki5.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
#----------------------------------Change Bio Command-------------------------------#
                            elif cmd.startswith("titanzbio:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = titanz.getProfile()
                                    profile.statusMessage = string
                                    titanz.updateProfile(profile)
                                    titanz.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("titanzbio1:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ki.getProfile()
                                    profile.statusMessage = string
                                    ki.updateProfile(profile)
                                    ki.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("titanzbio2:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ki2.getProfile()
                                    profile.statusMessage = string
                                    ki2.updateProfile(profile)
                                    ki2.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("titanzbio3:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ki3.getProfile()
                                    profile.statusMessage = string
                                    ki3.updateProfile(profile)
                                    ki3.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("titanzbio4:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ki4.getProfile()
                                    profile.statusMessage = string
                                    ki4.updateProfile(profile)
                                    ki4.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("titanzbio5:"):
                                if msg._from in Owner + admin:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ki5.getProfile()
                                    profile.statusMessage = string
                                    ki5.updateProfile(profile)
                                    ki5.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
#------------------------------Respon Command--------------------------#
                            elif text.lower() == "respon":
                                    titanz.sendMessage(msg.to, "sᴇᴘʀɪ ᴘʀᴏᴛᴇᴄᴛ ᴡᴀs ʜᴇʀᴇ")
                                    ki.sendMessage(msg.to, "sᴇᴘʀɪ ᴘʀᴏᴛᴇᴄᴛ ᴡᴀs ʜᴇʀᴇ")
                                    ki2.sendMessage(msg.to, "sᴇᴘʀɪ ᴘʀᴏᴛᴇᴄᴛ ᴡᴀs ʜᴇʀᴇ")
                                    ki3.sendMessage(msg.to, "sᴇᴘʀɪ ᴘʀᴏᴛᴇᴄᴛ ᴡᴀs ʜᴇʀᴇ")
                                    ki4.sendMessage(msg.to, "sᴇᴘʀɪ ᴘʀᴏᴛᴇᴄᴛ ᴡᴀs ʜᴇʀᴇ")
                                    titanz1.sendMessage(msg.to, "ʀᴇᴀᴅʏ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ")
                            elif text.lower() == 'clearban':
                                if msg._from in Owner:
                                    settings["blacklist"] = {}
                                    titanz.sendMessage(msg.to,"Blacklist Dibersihkan")
#------------------------------Join Command---------------------------#
                            elif text.lower() in ["Masuk"]:
                                if msg._from in Owner:    
                                    G = titanz.getGroup(msg.to)
                                    ginfo = titanz.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    titanz.updateGroup(G)
                                    invsend = 0
                                    Ticket = titanz.reissueGroupTicket(msg.to)
                                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    titanz1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    G = titanz.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    titanz.updateGroup(G)
                                    G.preventedJoinByTicket(G)
                                    titanz.updateGroup(G)
                            elif text.lower() in ["byeall"]:
                                if msg._from in Owner:   								
                                    ki.leaveGroup(msg.to)
                                    ki2.leaveGroup(msg.to)
                                    ki3.leaveGroup(msg.to)
                                    ki4.leaveGroup(msg.to)
                                    titanz1.leaveGroup(msg.to)	
#-------------------------------Protect Command-------------------------------#
                            elif text.lower() == 'protect on':
                                if msg._from in admin and Owner:
                                        if settings["protect"] == True:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Already On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Set To On")
                                        else:
                                            settings["protect"] = True
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Set To On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Already On")
                            elif text.lower() == 'protect off':
                                if msg._from in admin and Owner:
                                        if settings["protect"] == False:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Already Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Set To Off")
                                        else:
                                            settings["protect"] = False
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Set To Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Already Off")
                            elif text.lower() == 'qrprotect on':
                                if msg._from in admin and Owner:
                                        if settings["qrprotect"] == True:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection QR Already On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection QR Set To On")
                                        else:
                                            settings["qrprotect"] = True
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection QR Set To On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection QR Already On")
                            elif text.lower() == 'cancelprotect on':
                                if msg._from in admin and Owner:
                                        if settings["cancelprotect"] == True:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Already On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Set To On")
                                        else:
                                            settings["cancelprotect"] = True
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Set To On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Already On")
                            elif text.lower() == 'cancelprotect off':
                                if msg._from in admin and Owner:
                                        if settings["cancelprotect"] == False:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Already Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Set To Off")
                                        else:
                                            settings["cancelprotect"] = False
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Set To Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Cancel Already Off")
                            elif text.lower() == 'invprotect on':
                                if msg._from in admin and Owner:
                                        if settings["inviteprotect"] == True:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Already On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Set To On")
                                        else:
                                            settings["inviteprotect"] = True
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Set To On")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Already On")
                            elif text.lower() == 'invprotect off':
                                if msg._from in admin and Owner:
                                        if settings["inviteprotect"] == False:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Already Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                                        else:
                                            settings["inviteprotect"] = False
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection Invite Already Off")
                            elif text.lower() == 'qrprotect off':
                                if msg._from in admin and Owner:
                                        if settings["qrprotect"] == False:
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection QR Already Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection QR Set To Off")
                                        else:
                                            settings["qrprotect"] = False
                                            if settings["lang"] == "JP":
                                                titanz.sendMessage(msg.to,"➲ Protection QR Set To Off")
                                            else:
                                                titanz.sendMessage(msg.to,"➲ Protection QR Already Off")
                            elif text.lower() == 'setpro on':
                                if msg._from in Owner + admin:
                                    settings["protect"] = True
                                    settings["qrprotect"] = True
                                    settings["inviteprotect"] = True
                                    settings["cancelprotect"] = True
                                    titanz.sendMessage(msg.to," All Protection Set To On")
                                else:
                                    titanz.sendMessage(msg.to,"Just for Owner")
                            elif text.lower() == 'setpro off':
                                if msg._from in Owner + admin:
                                    settings["protect"] = False
                                    settings["qrprotect"] = False
                                    settings["inviteprotect"] = False
                                    settings["cancelprotect"] = False
                                    titanz.sendMessage(msg.to," All Protect Set To Off")
                                else:
                                    titanz.sendMessage(msg.to,"Just for Owner")
#------------------------------Owner , Staff List------------------------------#
                            elif msg.text in ["Ownerlist","ownerlist"]:
                                if Owner == []:
                                    titanz.sendMessage(msg.to,"The Ownerlist is empty")
                                else:
                                    titanz.sendMessage(msg.to,"Tunggu...")
                                    mc = ""
                                    mc = "╔══[ Owner Titanz Bot Protect ]"
                                    for mi_d in Owner:
                                        mc += "\n╠ "+titanz.getContact(mi_d).displayName + "\n"
                                    mc += "╚══[ Finish ]"
                                    titanz.sendMessage(msg.to,mc)
                            elif msg.text in ["Stafflist","stafflist"]:
                                if admin == []:
                                    titanz.sendMessage(msg.to,"The stafflist is empty")
                                else:
                                    titanz.sendMessage(msg.to,"Tunggu...")
                                    mc = ""
                                    mc = "╔══[ Staff Titanz Bot Protect ]"
                                    for mi_d in admin:
                                        mc += "\n╠ "+titanz.getContact(mi_d).displayName + "\n"
                                    mc += "╚══[ Finish ]"
                                    titanz.sendMessage(msg.to,mc)
#------------------------------Owner Add , Del---------------------------------#
                            elif "Owner add @" in msg.text:
                                if msg._from in Owner:
                                    print ("[Command]Owner add executing")
                                    _name = msg.text.replace("Owner add @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = titanz.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = ki2.getGroup(msg.to)
                                    gs = ki3.getGroup(msg.to)
                                    gs = ki4.getGroup(msg.to)
                                    gs = ki5.getGroup(msg.to)
                                    gs = titanz1.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            titanz.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                Owner.append(target)
                                                titanz.sendMessage(msg.to,"Owner Ditambahkan")
                                            except:
                                                pass
                                    print ("[Command]Owner add executed")
                                else:
                                    titanz.sendMessage(msg.to,"Command denied.")
                                    titanz.sendMessage(msg.to,"Owner permission required.")
                            elif "Owner del @" in msg.text:
                                if msg._from in Owner:
                                    print ("[Command]Owner del executing")
                                    _name = msg.text.replace("Owner del @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = titanz.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = ki2.getGroup(msg.to)
                                    gs = ki3.getGroup(msg.to)
                                    gs = ki4.getGroup(msg.to)
                                    gs = titanz1.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                        if targets == []:
                                            titanz.sendMessage(msg.to,"Contact not found")
                                    else:
                                        for target in targets:
                                            try:
                                                Owner.remove(target)
                                                titanz.sendMessage(msg.to,"Owner Dihapus")
                                            except:
                                                pass
                                    print ("[Command]Owner del executed")
                                else:
                                    titanz.sendMessage(msg.to,"Command denied.")
                                    titanz.sendMessage(msg.to,"Owner permission required.")
#------------------------------Pembatas Script---------------------------------#
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = titanz.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            titanz.updateProfilePicture(path)
                            titanz.sendMessage(to, "Berhasil mengubah foto profile")
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = ki.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            ki.updateProfilePicture(path)
                            ki.sendMessage(to, "Berhasil mengubah foto profile")
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = ki2.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            ki2.updateProfilePicture(path)
                            ki3.sendMessage(to, "Berhasil mengubah foto profile")
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = ki3.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            ki3.updateProfilePicture(path)
                            ki3.sendMessage(to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = titanz.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                titanz.updateGroupPicture(to, path)
                                titanz.sendMessage(to, "Berhasil mengubah foto group")
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
                            titanz.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = titanz.getContact(msg.contentMetadata["mid"])
                                if titanz != None:
                                    cover = titanz.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    titanz.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔══[ Details Contact ]"
                                ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╚══[ Finish ]"
                                titanz.sendMessage(to, str(ret_))
                            except:
                                titanz.sendMessage(to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = titanz.getContact(sender)
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
                                titanz.sendMessage(to, str(ret_))
                            except:
                                titanz.sendMessage(to, "🙄🙄🙄")
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
                        if sender != titanz.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        titanz.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            titanz.sendMessage(msg.to,text)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                titanz.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                titanz.log("[{} : {}]".format(str(msg.to), str(msg.text)))
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
                                    group = titanz.findGroupByTicket(ticket_id)
                                    titanz.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    titanz.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))

                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if titanzMid in mention["M"]:
                                        if settings["autoRespon"] == True:
                                            sendMention(sender, "Oi Asw @!,jangan main tag tag", [sender])
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
        ops = titanzPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                titanzPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
