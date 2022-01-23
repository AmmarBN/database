try:
    import os,sys,time,requests,mechanize
except:
       print ("Instalation Database")
       print ("Starting Installation..")
       time.sleep(3)
       print ("Mengimport Ulang Database")
       time.sleep(5)
       os.system ("pip install requests")
       print ("Done Install Data")
       os.system ("pip2 install requests")
       print ("Open File...")
       time.sleep(6)
os.system("clear")
print ("\033[1;96mSubscribe Dan Like Dulu Channel Admin")
os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
time.sleep(5)
os.system("clear")

# mengetik otomatis
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

localtime = time.asctime(time.localtime(time.time()))

# Buat Nanya
def nanya():
    a = raw_input("do you want more? [Y/T] ~~> ")
    if a =="Y" or a =="y":
	os.system("python2 Script-Bot.py")
    elif a =="T" or a =="t":
        os.system("exit")
        os.system("figlet Thank You For Using This Script")
print
# logo
banner = ("""\033[1;96m ___  ____ ___  ____ ____ ____ _ ___  ___
 |__] |  |  |   [__  |    |__/ | |__]  |
 |__] |__|  |   ___] |___ |  \ | |     | \033[1;90mMade With AmmarBN
\033[1;\033[1;90m
Untuk Menyalin Script Membutuhkan Koneksi Internet [!]
\033[1;0m
<---------[\033[1;0m\033[1;41mInfo Tools\033[1;0m]--------->
\033[1;96m Status Tools \033[1;90m: \033[1;92m Online
\033[1;96m Pengguna Tools \033[1;90m: \033[1;95m1 \033[1;90morang """)
print
print (banner)
print ("\033[1;96m Waktu \033[1;90m: \033[1;92m"+localtime)
print ("""\033[1;96m Note \033[1;90m: \033[1;92m Dilarang Decode Script""")
print ("\033[1;0m<---------[\033[1;0m\033[1;41mInformation\033[1;0m]--------->")
print ("""Tools Ini Akan Update Dengan Sendirinya Ketika Script/data Bot
Diubah Maka Tools Ini Juga Akan Berubah Dengan Sendirinya Dan
Kebalikannya Jika Data Botz Terhapus Maka Script Ini Tidak Dapat
Menemukan Web Data Botz Yang Disimpan/Hilang [!]""")
print ("<---------[\033[1;0m\033[1;41mMenu Botz Script\033[1;0m]--------->")
print ("\033[1;\033[1;90m1. \033[1;92mLord Botz")
print ("\033[1;\033[1;90m2. \033[1;92mAlpha Botz")
print
#Buat Input
pilihgan = input("\033[1;\033[1;90mInput Option : ")
if pilihgan == 1:
        print ("\033[1;\033[1;90mStarting.....")
	time.sleep(5)
        print ("""\033[1;93m1.handler.js
2.index.js
3.test.js
4.server.js
5.resetuser.js
6.package.json
7.package-lock.json
8.Dockerfile
9.LICENSE
10.Procfile
11.app.json
12.README.md
13.config.js (Bagian Penyetingan Owner)
14.database.json (Free 300 Database Lord Botz)
15.install.sh (Untuk Install Module)
16.main.js
17.lib (Folder Format)
18.plugins (Folder Format)
19.src (Folder Format)
20.tmp (Folder Format)
21.views (Folder Format)
""")
	pil = input("\033[1;\033[1;90mYour Options : \033[1;97m")
	if pil == " ":
		print ("Tidak Ada Pilihan!!")
		time.sleep(2)
		os.system("python2 Script-Bot.py")
	if pil == 1:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/handler.js")
		nanya()
	if pil == 2:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/index.js")
		nanya()
	if pil == 3:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/test.js")
		nanya()
	if pil == 4:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/server.js")
		nanya()
	if pil == 5:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/resetuser.js")
		nanya()
	if pil == 6:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/package.json")
		nanya()
	if pil == 7:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/package-lock.json")
		nanya()
	if pil == 8:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/Dockerfile")
		nanya()
	if pil == 9:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/LICENSE")
		nanya()
	if pil == 10:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/Procfile")
		nanya()
	if pil == 11:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/app.json")
		nanya()
	if pil == 12:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/README.md")
		nanya()
	if pil == 13:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/config.js")
		nanya()
	if pil == 14:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/database.json")
		nanya()
	if pil == 15:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/install.sh")
		nanya()
	if pil == 16:
		os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/main.js")
		nanya()
#lib
	if pil == 17:
		print ("""1.cloudDBAdapter.js
2.converter.js
3.exif.json
4.gdrive.js
5.jagokata.js
6.levelling.js
7.logs.js
8.mongoDB.js
9.print.js
10.scrape_joox.js
11.simple.js
12.sticker.js
13.tictactoe.d.ts
14.tictactoe.js
15.uploadFile.js
16.uploadImage.js
17.webp2mp4.js
18.welcome.js
19.y2mate.js
20.lowdb (Folder Format)""")
		you = input("\033[1;\033[1;90mYour Options : ")
		if you == 1:
			os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/cloudDBAdapter.js")
			nanya()
		if you == 2:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/converter.js")
			nanya()
		if you == 3:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/exif.json")
			nanya()
		if you == 4:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/gdrive.js")
			nanya()
		if you == 5:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/jagokata.js")
			nanya()
		if you == 6:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/levelling.js")
			nanya()
		if you == 7:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/logs.js")
			nanya()
		if you == 8:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/mongoDB.js")
			nanya()
		if you == 9:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/print.js")
			nanya()
		if you == 10:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/scarape_joox.js")
			nanya()
		if you == 11:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/simple.js")
			nanya()
		if you == 12:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/sticker.js")
			nanya()
		if you == 13:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/tictactoe.d.ts")
			nanya()
		if you == 14:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/tictactoe.js")
			nanya()
		if you == 15:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/uploadFile.js")
			nanya()
		if you == 16:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/uploadImage.js")
			nanya()
		if you == 17:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/webp2mp4.js")
			nanya()
		if you == 18:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/welcome.js")
			nanya()
		if you == 19:
                        os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lib/y2mate.js")
			nanya()
#lib/#lowdb
		if you == 20:
                        print ("""1.adapters (Folder Format

2.Low.d.ts
3.Low.js
4.LowSync.d.td
5.LowSync.js
6.MissingAdapterError.d.ts
7.MissingAdapterError.js
8.index.d.ts
9.index.js.""")
			lord = input("Input Menu ~> ")
			if lord == 1:
				print ("belum")
			if lord == 2:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/Low.d.ts")
				nanya()
			if lord == 3:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/Low.js")
				nanya()
			if lord == 4:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/LowSync.d.ts")
				nanya()
			if lord == 5:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/LowSync.js")
				nanya()
			if lord == 6:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/MissingAdapterError.d.ts")
				nanya()
			if lorr == 7:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/MissingAdapterError.js")
				nanya()
			if lord == 8:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/index.d.ts")
				nanya()
			if lord == 9:
				os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/lowdb/index.js")
				nanya()
#Folder lib Selesai Atau Tamat
#new folder
#plugins
	if pil == 18:
		print ("""\033[1;92mGrup-seting.js       calc.js              ilham.js             profile.js                tebakkata.js
_afk.js              carigrup.js          img2braille.js       promote.js                tebakkata_ans.js
_anonymous_chat.js   caripesan.js         infoCmdWithMedia.js  qrcode.js                 tebakkata_hint.js
_antilink.js         case.js              inspectlink.js       quotemaker.js             tebakkimia.js
_antispam.js         ceksn.js             itssostupid.js       quotemaker2.js            tebakkimia_ans.js
_antisticker.js      charainfo.js         jadian.js            quotes.js                 tebakkimia_hint.js
_antitoxic.js        citacita.js          jadibot.js           randomloli.js             tebaklagu.js
_antitroli.js        clear.js             jodoh.js             readmore.js               tebaklagu_ans.js
_antiviewonce.js     cmdWithMedia.js      join.js              readviewonce.js           tebaklagu_hint.js
_antivirus.js        colorful.js          joox.js              referal.js                tebaklirik.js
_autodelvnbot.js     contact.js           kapankah.js          register.js               tebaklirik_ans.js
_autolevelup.js      covid.js             kapankah2.js         renungan.js               tebaklirik_hint.js
_buttonResponse.js   creator.js           katabijak.js         report.js                 template.js
_ephemeral.js        customtrigger.js     kbbi.js              retro.js                  textpro.js
_getmsg.js           dadu.js              koboy.js             revoke.js                 tictactoe.js
_role.js             daily.js             kodenuklir.js        runningtext.js            tiktok.js
_simi.js             dare.js              kodenuklir2.js       salat.js                  togif.js
_tictactoe.js        darkjoke.js          kodepos.js           scan.js                   toimg.js
absen-cekabsen.js    debounce.js          layarkaca.js         script.js                 toimg2.js
absen-delete.js      delCmdWithMedia.js   leaderboard.js       semoji.js                 tomp3.js
absen-start.js       delete.js            leavegc.js           sendquote.js              toptt.js
absen.js             delmsg.js            levelup.js           setCmdWithMedia.js        totalPesan.js
accbang.js           delprem.js           limit.js             setProfileGroup.js        tovideo.js
add.js               delsesittt.js        link.js              setbotbio.js              translate.js
addWhitelist.js      demote.js            listCmdWithMedia.js  setbotname.js             trendingtwitter.js
addmsg.js            donasi.js            listjadibot.js       setbotpp.js               trigger.js
addprem.js           enable.js            listmsg.js           setbye.js                 truth.js
afk.js               enhance.js           listprem.js          setdesk_gc.js             ttp.js
aksara.js            enphoto360.js        lockCmdWithMedia.js  setmenu.js                ttp2.js
akungratis.js        exec.js              lockmsg.js           setname_gc.js             ttpdark.js
alkitab.js           exec2.js             lolice.js            setwelcome.js             tts.js
alquran.js           family100.js         lyrics.js            shaun_the_sheep_photo.js  twitter.js
animeinfo.js         family100_answer.js  magernulis.js        siapakahaku.js            unbanchat.js
anonymous_chat.js    fb.js                mangainfo.js         siapakahaku_ans.js        unbanuser.js
apakah.js            fetch.js             masak.js             siapakahaku_hint.js       unregister.js
apakah2.js           fitnah.js            math.js              simpcard.js               unsplah.js
army.js              gay.js               math_answer.js       simsimi.js                update.js
artinama.js          generate_nama.js     megumin.js           simulate.js               update2.js
asahotak.js          generate_purba.js    meme.js              smule.js                  upload.js
asahotak_ans.js      getcode.js           memeg.js             snackvideo.js             upsw.js
asahotak_hint.js     getexif.js           mention.js           spamcall.js               voicechanger.js
asmaulhusna.js       getsider.js          menu.js              speed.js                  vote-cekvote.js
asupan.js            gimage.js            modapk.js            spotify.js                vote-delete.js
attp.js              gitclone.js          neko.js              ssweb.js                  vote-start.js
attp2.js             github-search.js     news.js              sticker.js                vote-vote.js
banchat.js           githubdl.js          nulis2.js            stickerLine.js            waifu.js
bannedList.js        glowing.js           odemote.js           stickerTelegram.js        wait.js
banuser.js           google.js            okick.js             stickerly.js              wallpaperAnime.js
base64.js            groupInfo.js         online.js            stickfilter.js            wallq.js
blockList.js         grouplist.js         opengumuman.js       stickmaker.js             warning.js
bokep.js             hacker.js            opromote.js          stopjadibot.js            warning_cek.js
bold.js              hadis.js             pantun.js            styletext.js              warning_del.js
brainly.js           hlh.js               pay.js               subreddit.js              wikipedia.js
broadcast.js         hornycard.js         paylimit.js          sudo.js                   wm.js
broadcastgroups.js   ht.js                pengumuman.js        suitpvp.js                yt-comment.js
broadcastjadibot.js  hug.js               pickk.js             suitpvp_ans.js            yta.js
bucin.js             idfreefire.js        pikachu.js           tagall.js                 yts.js
buylimit.js          ig.js                pinterest.js         tahta2.js                 ytv.js
caklontong.js        ighightlight.js      play.js              tebakgambar.js            zodiac.js
caklontong_ans.js    igstalk.js           poly.js              tebakgambar_answer.js     zodiak_harian.js
caklontong_hint.js   igstory.js           ppcouple.js          tebakgambar_hint.js       zodiak_mingguan.js""")
		ganz = raw_input("Masukkan Nama Script ~> ")
		print ("\033[1;96mhttps://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/plugins/"+ganz)
		print ("\033[1;97mSalin Text Diatas Lalu Masukkan Di Browser/Google")
		time.sleep(5)
		nanya()
#FOLDER PLUGINSNANO SUDAH TAMAT
#NEW FOLDER
#src
	if pil == 19:
		print ("""1.LICENSE
2.avatar_contact.png
3.welcome.svg
4.Aesthetic (Folder Format)
5.font (Folder Format)
6.kertas (Folder Format)""")
		src = input("Pilih Menu ~> ")
		if src == 1:
			os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/src/LICENSE")
			nanya()
		if src == 2:
			os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/src/avatar_contact.png")
			nanya()
		if src == 3:
			os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/src/welcome.svg")
			nanya()
#src/#Aesthetic
		if src == 4:
			print ("Aesthetic_000.jpeg  Aesthetic_001.jpg  Aesthetic_002.jpg")
			Aesthetic = raw_input("Masukkan Pilihan ~> ")
			print ("\033[1;96mhttps://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/src/Aesthetic/"+Aesthetic)
	                print ("\033[1;97mSalin Text Diatas Lalu Masukkan Di Browser/Google")
        	        time.sleep(5)
                	nanya()
#src/#font
		if src == 5:
			print ("""'Futura Bold Italic font.ttf'     Roboto-BoldItalic.ttf
Futura Bold font.ttf'            Roboto-Italic.ttf
Futura Book Italic font.ttf'     Roboto-Light.ttf
Futura Book font.ttf'            Roboto-LightItalic.ttf
Futura Extra Black font.ttf'     Roboto-Medium.ttf
Futura Heavy Italic font.ttf'    Roboto-MediumItalic.ttf
Futura Heavy font.ttf'           Roboto-Regular.ttf
Futura Light Italic font.ttf'    Roboto-Thin.ttf
Futura Light font.ttf'           Roboto-ThinItalic.ttf
Futura Medium Italic font.ttf'   Zahraaa.ttf
Futura XBlk BT.ttf'              futur.ttf
Futura-CondensedLight.otf        futura light bt.ttf
Roboto-Black.ttf                 futura medium bt.ttf
Roboto-BlackItalic.ttf           futura medium condensed bt.ttf
Roboto-Bold.ttf""")
			font = raw_input("Masukkan Pilihan ~> ")
			print ("\033[1;96mhttps://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/src/font/"+font)
                        print ("\033[1;97mSalin Text Diatas Lalu Masukkan Di Browser/Google")
                        time.sleep(5)
                        nanya()
#src/#kertas
		if src == 6:
			print ("magernulis1.jpg")
			kertas = raw_input("Masukkan Text Yang Ada Diatas : ")
			print ("\033[1;96mhttps://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/src/kertas/"+kertas)
                        print ("\033[1;97mSalin Text Diatas Lalu Masukkan Di Browser/Google")
                        time.sleep(5)
                        nanya()
#Folder SRC Sudah Selesai Atau Tamat
#New Folder
#tmp
	if pil == 20:
		print ("file")
		file = raw_input("Masukkan Text Yang Ada Diatas : ")
		print ("\033[1;96mhttps://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/tmp/file")
                print ("\033[1;97mSalin Text Diatas Lalu Masukkan Di Browser/Google")
		time.sleep(5)
                nanya()
#views
	if pil == 21:
		print ("""1.index.js 
2.index.html 
3.style.css 
4.img""")
		ha = input("Pilih : ")
		if ha == 1:
			os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/views/index.js")
			nanya()
		if ha == 2:
			os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/views/index.html")
			nanya()
		if ha == 3:
			os.system("xdg-open https://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/views/style.css")
			nanya()
#views/#img
		if ha == 4:
			print ("1.dark  2.light")
			img = input("Pilih Menu : ")
#views/#img/#dark
			if img == 1:
				print ("""Tes                                 balloon_incoming_pressed_ext.9.png
balloon_centered_normal.9.png       balloon_live_location_incoming_frame.9.png
balloon_centered_pressed.9.png      balloon_live_location_outgoing_frame.9.png
balloon_centered_shadow.9.png       balloon_outgoing_frame.9.png
balloon_incoming_frame.9.png        balloon_outgoing_normal.9.png
balloon_incoming_normal.9.png       balloon_outgoing_normal_ext.9.png
balloon_incoming_normal_ext.9.png   balloon_outgoing_normal_stkr.9.png
balloon_incoming_normal_stkr.9.png  balloon_outgoing_pressed.9.png
balloon_incoming_pressed.9.png      balloon_outgoing_pressed_ext.9.png""")
				dark = raw_input("Pilih Salah Satu Text : ")
				print ("\033[1;96mhttps://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/views/img/dark/"+dark)
				print ("\033[1;97mSalin Text Diatas Lalu Masukkan Di Browser/Google")
        	                time.sleep(5)
                	        nanya()
			if img == 2:
#views/#img/#light
				print ("""Tes                                 balloon_incoming_pressed_ext.9.png
balloon_centered_normal.9.png       balloon_live_location_incoming_frame.9.png
balloon_centered_pressed.9.png      balloon_live_location_outgoing_frame.9.png
balloon_centered_shadow.9.png       balloon_outgoing_frame.9.png
balloon_incoming_frame.9.png        balloon_outgoing_normal.9.png
balloon_incoming_normal.9.png       balloon_outgoing_normal_ext.9.png
balloon_incoming_normal_ext.9.png   balloon_outgoing_normal_stkr.9.png
balloon_incoming_normal_stkr.9.png  balloon_outgoing_pressed.9.png
balloon_incoming_pressed.9.png      balloon_outgoing_pressed_ext.9.png""")
				light = raw_input("Pilih Salah Satu Text : ")
				print ("\033[1;96mhttps://raw.githubusercontent.com/AmmarBN/lordbot-aq-tes/master/views/img/light"+light)
				print ("\033[1;97mSalin Text Diatas Lalu Masukkan Di Browser/Google")
                                time.sleep(5)
                                nanya()
if pilihgan == 2:
      print ("Coming Soon")
      time.sleep(5)
      os.system("clear")
      os.system("figlet Thank You For Using This Script")
	    
	
