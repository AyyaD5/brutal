import requests
import time,os,sys,time,requests
from time import sleep

a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

#logo
os.system('clear')
print ('\033[36mSave Wa gua tod\033[37mhehe \033[36mok! :v')
os.system('wa.me/6285871678067')
sleep(4)
os.system('clear')
print ('\033[36mJoin Grub \033[37Jowo_Xclusive')
os.system('termux-open-url https://cararegistrasi.com/bvC8MF')
sleep(3)
os.system('clear')
banner= """
\033[37m    __      _____     __    __     \033[94m    _____
\033[37m   / /_    / ___ \   /  \__/  \    \033[94m   / ___/____ ___  _____
\033[37m  / __ \  / /  / /  / /\    /\ \   \033[94m   \__ \/ __ `__ \/ ___/
\033[37m / /_/ / / /_ / /  / /  \__/  \ \  \033[94m  ___/ / / / / / (__  )
\033[37m/_____/  \_____/  /_/          \_\ \033[94m /____/_/ /_/ /_/____/
\033[37m
\033[32m[•]───────────────────────────────────────────[•]
\033[32m | \033[94m[+]  \033[32mAuthor  : \033[35mAyyaGans:)                    \033[32m |
\033[32m | \033[33m[+]  \033[32mTEAM    : \033[33mJOWO_XCLUSIVE           \033[32m |
\033[32m | \033[35m[+]  \033[32mChanel  : \033[35mAyyaD5                  \033[32m |
\033[32m[•]───────────────────────────────────────────[•]"""
os.system('clear')
print (banner)

print
print ('\033[31mNomor awali dari : \033[94m 8xxxx')


#Run nomor

nomor = input(' \033[33mNomer Togel atau mantan :\033[90m ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
     print (' \033[32m[√] \033[94mhore berhasil viuwit :) ')
else:
     print (' \033[31m[¡] \033[94myahahah gagal su :( ')
