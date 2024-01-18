# Uses Pickle,Os,getpass Modules

import random,pickle,os,getpass
import tkinter as tk
import PySimpleGUI as sg
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
try:
    ndf=getpass.getuser()
    img=resource_path("logo_GUI.png")   # SPLASH SCREEN
    icon_use=resource_path("encrypt-removebg-preview.png") # ICON
    icon_resized=resource_path("re_ncrypt-removebg-preview.png") # ICON RESIZED
    DISPLAY_TIME_MILLISECONDS=4000
    #sg.popup_notify("HI")
    window=sg.Window("Encrypt_Decrypt@16",[[sg.Image(img)]],transparent_color=sg.theme_background_color(),no_titlebar=True,
                     keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS,close=True)
    sg.SystemTray.notify('Encrypt_Decrypt@16', 'Checking for Elgibility...',icon=icon_resized)                                         # remove if not
    sg.SystemTray.notify(' Encrypt_Decrypt@16', ' Elgible for Running Encryptor_Decryptor@16')
    username=["pranav","govind","aaron"]
    password=["@GROUP6@"]
    stat="nil"
    while stat!="Enter":
        layout9=[[sg.Text()],[sg.Text()],[sg.Text("Enter Username")]+[sg.Input(default_text="username",size=(30,100))],[sg.Text()],[sg.Text("Enter Password")]+[sg.Input(key='Password', password_char='*',size=(30,100))]
                 ,[sg.Text()],[sg.Button("Login",button_color="green2",size=(10,1),bind_return_key=True)]+[sg.Button("Exit",button_color="red",size=(10,1),bind_return_key=True)]]
        window9=sg.Window("Login",layout9,element_justification='r',size=(290,260),icon=icon_use)
        event,values=window9.read()
        window9.close()
        if event == "Login":
            if values[0] in username and values['Password'] in password:
                stat="Enter"
            else:
                window=sg.Window("Login Failed",[[sg.Text("\n\n\t     Login Failed.\n \tBad Login Credentials\t\n\n",text_color="Black",background_color="yellow")]],icon=icon_use).read(timeout=1500,close=True)
        else:
            exit()
    test=open("C:\\Users\\"+ndf+"\\Appdata\\Local\\Encrypt_Decrypt.txt","a")
    test.close()
    t=open("C:\\Users\\"+ndf+"\\Appdata\\Local\\Encrypt_Decrypt.txt","r")
    if t.readline()=="1":
        path=t.readline()
        t.close()
    else:
        t.close()
        t1=open("C:\\Users\\"+ndf+"\\Appdata\\Local\\Encrypt_Decrypt.txt","w")
        path = sg.popup_get_folder('Select folder to Save File')
        t1.write("1\n")
        path+="\\Encrypted_Encrypt_Decrypt.dat"
        t1.write(path)
        t1.close()
    theme=['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2',
           'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10',
           'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16',
           'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6',
           'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2',
           'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen',
           'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6',
           'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12',
           'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5',
           'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1',
           'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7',
           'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10',
           'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6',
           'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray',
           'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2',
           'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1',
           'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3',
           'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1',
           'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5',
           'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2',
           'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow',
           'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach',
           'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
    theme1=random.choice(theme)
    sg.theme(theme1)
    def encrypt(m):
        re=""
        k=m[::-1]
        s={'a':']','b':'[','c':'{','d':'}','e':':','f':';','g':'"','h':'<','i':'>',
           'j':'?','k':'/','l':'+','m':'=','n':'-','o':'_','p':')','q':'*','r':'(',
           's':'&','t':'|','u':'$','v':'^','w':'#','x':'@','y':'!','z':'~',' ':'2',',':'5','.':'8'}
        for i in k:
            if i in s:
                re+=s[i]
            else:
                re+=i
        sg.popup_scrolled(re,title="Encrypted Text",background_color="white",text_color="Black",icon=icon_use)
        return re
    def decrypt(m2):
        r=""
        k2=m2[::-1]
        s2={']': 'a', '[': 'b', '{': 'c', '}': 'd', ':': 'e', ';': 'f', '"': 'g', '<': 'h',
            '>': 'i', '?': 'j', '/': 'k', '+': 'l', '=': 'm', '-': 'n', '_': 'o', ')': 'p',
            '*': 'q', '(': 'r', '&': 's', '|': 't', '$': 'u', '^':'v', '#': 'w', '@': 'x', '!': 'y',
            '~': 'z', '2': ' ','5':',','8':'.'}
        for i in k2:
            if i in s2:
                r+=s2[i]
            else:
                r+=i
        sg.popup_scrolled(r,title="Decrypted Text",background_color="white",text_color="Black",icon=icon_use)
        return r
    def storage(d):
        global path
        file=open(path,"ab")
        pickle.dump(d,file)
        file.close()
        layouts=[[sg.Text("$ Data Stored By Double Encryption Secure Lock System")],[sg.Button(">>>",bind_return_key=True)]]
        windows=sg.Window("Success",layouts,icon=icon_use)
        event,values=windows.read()
        windows.close()
    def show():
        global path
        file=open(path,"rb")
        dat=pickle.load(file)
        k=decrypt(dat)
    layout1=[[sg.Text("\n\n\t<<<<<<<<<<<<<<<<<<<<<<<<<<<<\t \n\t ENCRYPTOR-DECRYPTOR @ 16\t \n\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>\t\n\n")],[sg.Button(">>>",bind_return_key=True)]]
    window1=sg.Window("ENCRYPTOR-DECRYPTOR @ 16",layout1,icon=icon_use)
    event,values=window1.read()
    window1.close()
    layout2=[[sg.Text("\n\n\t* Version_3.0.0\t \n\n\te: Encrypt Text\n\td: Decrypt Text\t\n \n\t&& at end in Encrypt mode for Double Encryption Storage\t\n \t&& in Decrypt mode for Viewing Double Encryption Files\t\n \tUse / character to avoid && Execution\t\n\n")],[sg.Button(">>>",bind_return_key=True)]]
    window2=sg.Window("ENCRYPTOR-DECRYPTOR @ 16",layout2,icon=icon_use)
    event,values=window2.read()
    window2.close()
    while True:
        layout3=[[sg.Text("\n")],[sg.Button("Encrypt",size=(100,1),bind_return_key=True)],
                 [sg.Button("Decrypt",size=(100,1),bind_return_key=True)],[sg.Button("Exit",size=(100,1),button_color="red",bind_return_key=True)]]
        window3=sg.Window("ENCRYPTOR-DECRYPTOR @ 16",layout3,size=(290, 240),icon=icon_use)
        event,values=window3.read()
        window3.close()
        if event=="Encrypt":
            layout4=[[sg.Text("Enter the Text")],[sg.InputText()],[sg.Button("Encrypt",bind_return_key=True)]]
            window4=sg.Window("Encryptor",layout4,icon=icon_use)
            event,values=window4.read()
            window4.close()
            m=values[0]
            if len(m)>3:
                if m[-3]+m[-2]+m[-1]=="/&&":
                    rt=""
                    for i in m:
                        if i!="/":
                            rt+=i
                        else:
                            continue
                    encrypt(rt)
                elif m[-1]+m[-2]=="&&":
                    d=encrypt(m[:-2])
                    storage(d)
                else:
                    encrypt(m)
            else:
                encrypt(m)
        elif event=="Decrypt":
            layout5=[[sg.Text("Enter the Text")],[sg.InputText()],[sg.Button("Decrypt",bind_return_key=True)]]
            window5=sg.Window("Decryptor",layout5,icon=icon_use)
            event,values=window5.read()
            window5.close()
            m2=values[0]
            if m2=="&&":
                d=""
                show(d)
            elif m2=="/&&":
                decrypt(m2[1:])
            else:
                decrypt(m2)
        else:
            exit()
except PermissionError:
    icon_use=resouce_path("encrypt-removebg-preview.png") # ICON
    sg.popup("\n\n\tPlease Allow Permission for Writing\t\n\n",icon=icon_use)
except:
    icon_use=resource_path("encrypt-removebg-preview.png") # ICON
    sg.popup("\n\n\tAN ERROR HAD OCCURED IN THE PROGRAM...\t\n\n",icon=icon_use)
    sg.popup("\n\n\tExiting...\t\t\n\n",icon=icon_use)
