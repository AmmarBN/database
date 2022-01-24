import os
from time import sleep
from threading import Thread as td


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
d ='\033[1;90m'
e ='\033[1;95m'

class Terkey:
  def __init__(self):
    pass

  # Nanya
  def nanya(self):
      a = input("do you want more? [Y/T] ~~> ")
      if a =="Y" or a =="y":
          os.system("python3 keymux.py")
      elif a =="T" or a =="t":
          os.system("exit")
          os.system("figlet Thank You For Using This Script")

  # animasi
  def animasi(self):
      for i in "-\|/-\|/-|/-|/-\|/-|":
              print(f'\r{d}Starting {c}[{e}{i}{c}] ',end="",flush=True)
              sleep(0.1)

  # Installing Data
  def data(self):
      os.system('clear')
      print(f'{c}Installing File Data')
      os.system('pip install requests && pip2 install requests')
      print(f'{d}Done Installing File Data')
      sleep(2)

  # Banner
  def banner(self):
      os.system('clear')
      print(f'''{c} █░▄▀ █▀▀ ▀▄░▄▀ █▄░▄█ █░█ █░█
 █▀▄░ █▀▀ ░░█░░ █░█░█ █░█ ▄▀▄
 ▀░▀▀ ▀▀▀ ░░▀░░ ▀░░░▀ ░▀░ ▀░▀'''.center(68))
      print(f'{c}[{c}Key Termux{a}]')
      print(f'{a}Copyright By AmmarBN')
      print("".join([i for i in "\n"*2]))

  # Loading animation
  def animate(self,params):
    self.banner()
    print(f"{c}Setting up your keys..")
    t = td(target=self.setup,args=(params,))
    t.start()
    while t.is_alive():
          for i in "-\|/-\|/":
              print(f'\r{d}Starting {a}{i} ',end="",flush=True)
              sleep(0.1)
    self.banner()
    print(f"DONE !\n\n{c}Please run this tool again and select {a}About{c} menu\nfor more informations\nThanks !")

  # Of course, like it name, paginate !
  def paginate(self,data,n):
    n_data = round(len(data)/n) + 1
    new_data_part = []
    batas = 0
    for i in range(n_data):
      new_data = []
      for x in range(batas,n+batas):
        try:
          new_data.append(data[x])
        except:
          pass
        batas += 1
      if new_data: new_data_part.append(new_data)
    return new_data_part

  # setting up the selected keys
  def setup(self,keys):
      keys = f"extra-keys = {keys}"
      try:
          os.mkdir('/data/data/com.termux/files/home/.termux')
      except:
          pass
      open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(keys)
      os.system('termux-reload-settings')

  # If you choose default keys, this function will be executed.
  def standar(self):
    key = "[['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    return key

  def about(self):
    self.banner()
    print(f"""
    {a}W E L C O M E  !{c}

    This is Terkey, Adalah Shorcut Dari Beberapa Kunci Termux !
    A program Creator from {a}AmmarBN{c} for you.
    This tool is only for Termux app and absolutely FREE !

    You can find all default keys in this program at
    {a}https://wiki.termux.com/wiki/Touch_Keyboard{c}

    Follow My Medsos ©AmmarBN
    * Instagram : {a}https://ig.me/lord_ammar_quoteser{c}
    * Guthub    : {a}https://github.com/AmmarBN{c}
    * Youtube   : {a}https://youtube.com/c/AmmarBN{c}

    {a}Copyright ©Saturday 22 January{c}

    """
    )
  # And if you select custom keys,
  def custom(self):
    index = 1
    lastindex = 0
    keys = ["CTRL","ALT","FN","SPACE","ESC","TAB","HOME","END","PGUP","PGDN","INS","DEL","BKSP","UP","LEFT","RIGHT","DOWN","ENTER","BACKSLASH","QUOTE","APOSTROPHE","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","KEYBOARD","DRAWER"]
    print(f"{a} --+ {c}「 Default Key Lists 」 {a}+--".center(62))
    print()
    for i in self.paginate([*enumerate(keys)],4):
      for x in i:
        en = " " * (15 - len(". ".join([str(x[0]+1),x[1]])))
        print(f"{a}{x[0]+1}.{c} {x[1]}",end=en)
      print()
    print(f"{c}\nInput your selected key number \nand sparate it by comma (,) {a}ex: 1,2,3,4{c}\nOr you can add your own custom key \nlike {a}1,2,3,(,),*,<,>{c} etc.")

    selected_keys = []
    user_select = input(f"\n{a}Input {c}: ")
    ranges = [str(i+1) for i in range(len(keys))]
    for i in user_select.split(","):
      if i.isdigit() and i in ranges:
        selected_keys.append(keys[int(i)-1])
      else:
        selected_keys.append(i)
    return selected_keys

  # Main
  def start(self):
    self.data()
    self.animasi()
    sleep(3)
    self.banner()
    print(f"    {a}❂╾╼╾╼╾╼[ {c} 「 Menu 」 {a}]╾╼╾╼╾╼❂")
    print(f"""  ╭♛
  {a}├►1.{c} Use Default Keys (All Key)
  {a}├►2.{c} Custom Keys (Input Key)
  {a}├►3.{c} About (Creator Biodata)
  {a}├►4.{c} Subscribe (Youtube Creator)
  {a}├►5.{c} Github (Github Creator)
  {a}╰───────────────
    """
    )
    menu = input(f"  {c}Input Your Option : {a} ")
    if menu == "1":
      self.banner()
      key = self.standar()
      self.animate(key)
    elif menu == "2":
      self.banner()
      key = self.custom()
      keys = self.paginate(key,7)
      print(f"{c}\nSelected keys: {a}{','.join(key)}{c}\nAre you sure ?")
      try:
        input(f"{c}Press enter to continue or CTRL + C to cancel ")
        self.animate(keys)
      except:
        exit(f"{b}Canceled!{c}")
    elif menu == "3":
      self.about()
    elif menu == "4":
      os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
      self.nanya()
    elif menu == "5":
      os.system("xdg-open https://github.com/AmmarBN")
      self.nanya()
    else:
      pass
if __name__=='__main__':
  terkey = Terkey()
  terkey.start()
# ini cuma shortcut buat bantu para decode Sampah🚮
# Copyright ©AmmarBN
