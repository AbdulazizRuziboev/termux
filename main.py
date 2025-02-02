import os
import sys
import time
import random
import json
import requests
from colorama import Fore, Style, init
import sys
#IF CODES
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#login
def login(email, password):
    url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'email': email, 'password': password, 'returnSecureToken': True}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get('idToken', None)
    return None  
#add_money
def add_money(request):
    money = input(Fore.YELLOW+"Enter Money Value: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "money": money,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    print("Get Money Activated ✅")
#addcoin
def add_coin(request):
    coin = input(Fore.YELLOW+"Enter Coin Value: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "coin": coin,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    print("Get Coin Activated ✅")
#get_king
def get_king(request):
    url = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"
    url_2 = "https://us-central1-cpm-2-7cea1.cloudfunctions.net/SetUserRating4_AppI"
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    }
    dd = {
    "data": "{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\" : 2000000000,\"gifts\" : 2000000000,\"transure\" : 2000000000,\"cars\" : 2000000000,\"levels\" : 2000000000,\"drift\" : 2000000000,\"run\" : 2000000000,\"police\" : 2000000000,\"block_post\" : 2000000000,\"real_estate\" : 2000000000,\"fuel\" : 2000000000,\"car_trade\" : 2000000000,\"car_exchange\" : 2000000000,\"burnt_tire\" : 2000000000,\"car_fix\" : 2000000000,\"car_wash\" : 2000000000,\"offroad\" : 2000000000,\"passanger_distance\" : 2000000000,\"reactions\" : 2000000000,\"drift_max\" : 2000000000,\"taxi\" : 2000000000,\"delivery\" : 2000000000,\"cargo\" : 2000000000,\"push_ups\" : 2000000000,\"slicer_cut\" : 2000000000,\"car_collided\" : 2000000000,\"new_type\" : 2000000000}}"}
    data = {
        "data":"{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\": 2000000000,\"gifts\": 2000000000,\"transure\": 2000000000,\"cars\": 137,\"levels\": 82,\"drift\": 2000000000,\"run\": 2000000000,\"police\": 2000000000,\"block_post\": 2000000000,\"real_estate\": 12,\"fuel\": 2000000000,\"car_trade\": 2000000000,\"car_exchange\": 2000000000,\"burnt_tire\": 2000000000,\"car_fix\": 2000000000,\"car_wash\": 2000000000,\"offroad\": 2000000000,\"passanger_distance\": 2000000000,\"reactions\": 2000000000,\"drift_max\": 2000000000,\"texi\": 2000000000,\"delivery\": 2000000000,\"cargo\": 2000000000,\"push_ups\": 2000000000,\"slicer_cut\":1,\"car_collided\":2000,\"new_type\": 2000}"
    }
    a = requests.post(url, headers=headers, json=dd)
    return a.text
#custom_id
def custom_id(request):
    custom_input = input(Fore.YELLOW+"Enter new ID: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "LocalID": custom_input,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    print("Custom ID Activated ✅")
    print("Custom ID Activated ✅")
def custom_name(request):
    custom_named = input(Fore.YELLOW+"Enter new ID: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "Name": custom_named,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    print("Custom Name Activated ✅")

def get_all(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "content-length": "4686",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    } 
    xx = {"data":"{\"allData\":\"ios7\",\"boughtFsos\":[-1],\"boughtPoliceLights\":[0,9,1,1,3,0,2,1,0,3,1,0],\"boughtPoliceSirens\":[1],\"FriendsID\":[],\"LevelsDoneTime\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"floats\":[169.0,188.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"integers\":[1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,15,0,0,0,0,0,0],\"fcar\":[0],\"favouriteWheels\":[],\"personEquipmentsMale.Gender\":1,\"personEquipmentsMale.bag\":[],\"personEquipmentsMale.beard\":[],\"personEquipmentsMale.cap\":[3,4,5],\"personEquipmentsMale.face\":[0],\"personEquipmentsMale.glasses\":[],\"personEquipmentsMale.gloves\":[],\"personEquipmentsMale.hair\":[3],\"personEquipmentsMale.mask\":[],\"personEquipmentsMale.pants\":[3],\"personEquipmentsMale.shoes\":[0],\"personEquipmentsMale.top\":[0],\"personEquipmentsMale.SelectedEquipments\":[-1,0,-1,3,-1,0,-1,-1,3,0,-1],\"personEquipmentsFemale.Gender\":1,\"personEquipmentsFemale.bag\":[],\"personEquipmentsFemale.beard\":[],\"personEquipmentsFemale.cap\":[],\"personEquipmentsFemale.face\":[],\"personEquipmentsFemale.glasses\":[],\"personEquipmentsFemale.gloves\":[],\"personEquipmentsFemale.hair\":[],\"personEquipmentsFemale.mask\":[],\"personEquipmentsFemale.pants\":[],\"personEquipmentsFemale.shoes\":[],\"personEquipmentsFemale.top\":[],\"personEquipmentsFemale.SelectedEquipments\":[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],\"platesData\":{\"allPlates\":[{\"plateId\":1,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":2,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":3,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":4,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":5,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":6,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]}]},\"carIDnStatus\":{\"carGeneratedIDs\":[\"PP046001_0EM520\",\"PP046001_1HZ434\",\"PP046001_2AI601\",\"PP046001_3XE666\",\"PP046001_4UE186\",\"PP046001_5PT234\",\"PP046001_6YX838\",\"PP046001_7LX480\",\"PP046001_8DS116\",\"PP046001_9NX832\",\"PP046001_10WK456\",\"PP046001_11TD028\",\"PP046001_12ND577\",\"PP046001_13DV244\",\"PP046001_14AG741\",\"PP046001_15BS263\",\"\",\"PP046001_17LK238\",\"PP046001_18JF051\",\"PP046001_19KX803\",\"PP046001_20GZ586\",\"PP046001_21UF017\",\"PP046001_22YP130\",\"PP046001_23FN836\",\"PP046001_24HC607\",\"\",\"\",\"PP046001_27RX784\",\"PP046001_28KK142\",\"PP046001_29WE007\",\"PP046001_30PD713\",\"PP046001_31RE817\",\"PP046001_32YY233\",\"\",\"\",\"PP046001_35VU702\",\"\",\"PP046001_37GL131\",\"\",\"PP046001_39TJ356\",\"PP046001_40FW772\",\"PP046001_41EU384\",\"PP046001_42WG860\",\"PP046001_43BS150\",\"PP046001_44WH827\",\"PP046001_45FH475\",\"\",\"PP046001_47UJ768\",\"PP046001_48TV341\",\"PP046001_49JN530\",\"\",\"PP046001_51QD838\",\"\",\"PP046001_53YV825\",\"PP046001_54GJ675\",\"PP046001_55ML516\",\"PP046001_56SJ686\",\"PP046001_57LH242\",\"PP046001_58MP057\",\"PP046001_59AZ262\",\"PP046001_60JU068\",\"PP046001_61SD005\",\"PP046001_62PN525\",\"\",\"\",\"PP046001_65TK146\",\"PP046001_66QD778\",\"\",\"\",\"\",\"PP046001_70ZC458\",\"\",\"\",\"\",\"PP046001_74AX427\",\"\",\"PP046001_76QU426\",\"PP046001_77YK376\",\"\",\"\",\"\",\"PP046001_81GH646\",\"PP046001_82IE441\",\"\",\"\",\"PP046001_85WP652\",\"PP046001_86YN631\",\"PP046001_87CN364\",\"PP046001_88UP157\",\"PP046001_89ZN352\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"_99CE612\",\"PP046001_100ZW228\",\"PP046001_101IA561\",\"PP046001_102UU717\",\"PP046001_103PY155\",\"PP046001_104IX462\",\"PP046001_105MM263\",\"PP046001_106XQ521\",\"PP046001_107AL041\",\"PP046001_108CS818\",\"PP046001_109SP418\",\"PP046001_110UZ317\",\"PP046001_111EI323\",\"PP046001_112UW055\",\"PP046001_113RE516\",\"PP046001_114IU002\",\"PP046001_115RY424\",\"PP046001_116TC480\",\"PP046001_117BK850\",\"PP046001_118LQ005\",\"\",\"PP046001_120BL584\",\"PP046001_121AC887\",\"\",\"PP046001_123LQ316\",\"PP046001_124ND278\",\"PP046001_125TF635\",\"PP046001_126JW025\",\"PP046001_127DT758\",\"PP046001_128FJ077\",\"PP046001_129HK434\",\"PP046001_130XW543\",\"PP046001_131KV244\",\"PP046001_132BD828\",\"PP046001_133HL267\",\"PP046001_134MX336\",\"PP046001_135SE266\",\"PP046001_136PL387\",\"PP046001_137II563\",\"PP046001_138AV428\",\"PP046001_139YP064\",\"PP046001_140EI273\",\"PP046001_141ZW243\",\"PP046001_142MF631\",\"PP046001_143GZ785\",\"PP046001_144XG274\",\"PP046001_145PS766\",\"PP046001_146VP038\",\"PP046001_147XW868\",\"PP046001_148TS261\",\"PP046001_149CC143\",\"PP046001_150LH203\",\"PP046001_151EA023\",\"PP046001_152RE265\",\"PP046001_153WC743\",\"PP046001_154SM847\",\"PP046001_155XR248\",\"PP046001_156CP055\",\"PP046001_157II684\",\"PP046001_158PH630\",\"PP046001_159WR786\",\"PP046001_160TN826\",\"PP046001_161ZB761\",\"PP046001_162AN531\",\"PP046001_163AV585\",\"PP046001_164LX861\",\"PP046001_165YL448\",\"PP046001_166MT276\",\"\",\"PP046001_168IP887\",\"PP046001_169IQ177\",\"PP046001_170EV155\",\"PP046001_171GP661\",\"PP046001_172WP866\",\"\",\"\",\"PP046001_175ZA568\",\"PP046001_176EQ523\",\"PP046001_177VG000\",\"PP046001_178YP367\",\"PP046001_179WS654\",\"PP046001_180GQ561\",\"PP046001_181IH643\",\"PP046001_182FH072\",\"PP046001_183TE720\",\"PP046001_184QM888\",\"PP046001_185JI650\",\"PP046001_186DZ572\",\"PP046001_187QN161\",\"PP046001_188SJ663\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"],\"carStatus\":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},\"flags\":{},\"animations\":[1,2,3,4],\"wheels\":[73,74,79,88,84,87,97,98,101]}"}

    print(xx['data'])

    a = requests.post(url, headers=headers, json=xx)
    return a

print(Fore.BLUE + """
     ██████╗██████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██╔════╝██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║     ██████╔╝██╔████╔██║       ██║   ██║   ██║██║   ██║██║     ███████╗  
    ██║     ██╔═══╝ ██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║          ██|  
    ╚██████╗██║     ██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
     ╚═════╝╚═╝     ╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    
      """)
email=input(Fore.LIGHTRED_EX+"✉️  Emailni kirgizing: ")
password=input(Fore.LIGHTRED_EX+"🔒 Parolni kirgizing: ")
token = login(email, password)
clear_screen()
banner = print(Fore.BLUE + """
     ██████╗██████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██╔════╝██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║     ██████╔╝██╔████╔██║       ██║   ██║   ██║██║   ██║██║     ███████╗  
    ██║     ██╔═══╝ ██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║          ██|  
    ╚██████╗██║     ██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
     ╚═════╝╚═╝     ╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    
      """)
service_title = print(Fore.RED+"    ══════════════════════════[ S E R V I C E S ]═════════════════════════════")
service_menu = print(Fore.CYAN + """
#💸 GET MONEY ~ 1
#🪙  GET COIN  ~ 2
#👑 KING RANK ~ 3
#🆔 CUSTOM ID ~ 4
#👤 NICKNAME  ~ 5
#🔓 UNLOCK ALL ~ 6 
#📤 EXIT  ~ 0
""" + Style.RESET_ALL)
while True:
    command = input(Fore.YELLOW+"Enter choice >>> ")
    if command.lower() == "0":
        print(Fore.RED + "Programm finished")
        break
    if command.lower() == "1":
        init(add_money(token))
        print(Fore.GREEN + "Get Money Activated ✅")
    if command.lower() == "2":
        init(add_coin(token))
        print(Fore.GREEN + "Get Coin Activated ✅")
    if command.lower() == "3":
        init(get_king(token))
        print(Fore.GREEN + "King Rank Activated ✅")
    if command.lower() == "4":
        init(custom_id(token))
        print(Fore.GREEN + "Custom ID Success ✅")
    if command.lower() == "5":
        init(custom_name(token))
        print(Fore.GREEN + "Nickname Changed ✅")
    if command.lower() == "6":
        init(get_all(token)+Style.RESET_ALL)
        print(Fore.GREEN + "Unlock ALL ✅")
