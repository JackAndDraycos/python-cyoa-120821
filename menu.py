import random
import tkinter
import charData
root = tkinter.Tk()
root.title("First Game")
root.geometry("1280x720")
root.option_add("*Font", "Papyrus")

player = charData.creature()

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def createChar():
    clear_screen()
    root.rowconfigure(0,weight=0)
    root.columnconfigure(0,weight=0)
    root.columnconfigure(2,weight=1)
    c = tkinter.StringVar()
    c.set(charData.classes[random.randrange(0,len(charData.classes))])
    w = tkinter.StringVar()
    w.set(charData.get_stat_name(charData.weapons,1))
    a = tkinter.StringVar()
    a.set(charData.get_stat_name(charData.armors,(10,0)))

    #Display current stats on right side of page - Initial
    uName=tkinter.Label(root, text="Name: " + player.getName())
    uName.grid(row=1,column=2)
    uClass=tkinter.Label(root, text="Class: " + player.getClass())
    uClass.grid(row=2,column=2)
    uHealth=tkinter.Label(root, text="Health: " + str(player.getMaxHealth()))
    uHealth.grid(row=3,column=2)
    uWeapon=tkinter.Label(root, text="Weapon: " + player.getWeapon())
    uWeapon.grid(row=4,column=2)
    uAccu=tkinter.Label(root, text="Accuracy: " + str(player.getAgi()))
    uAccu.grid(row=5,column=2)
    uDam=tkinter.Label(root, text="Damage Threshold: d" + str(player.getDamage()) + " + " + str(player.getStr()))
    uDam.grid(row=6,column=2)
    uArmor=tkinter.Label(root, text="Armor: " + player.getArmor())
    uArmor.grid(row=7,column=2)
    uDodge=tkinter.Label(root, text="Dodge: " + str(player.getDodge()))
    uDodge.grid(row=8,column=2)
    uDef=tkinter.Label(root, text="Defense: " + str(player.getDefense()))
    uDef.grid(row=9,column=2)
    uStr=tkinter.Label(root, text="Strength: " + str(player.getStr()))
    uStr.grid(row=10,column=2)
    uAgi=tkinter.Label(root, text="Agility: " + str(player.getAgi()))
    uAgi.grid(row=11,column=2)
    uIntel=tkinter.Label(root, text="Intelligence: " + str(player.getIntel()))
    uIntel.grid(row=12,column=2)
    
    #Name entry and drop downs for gear - Left Side
    tkinter.Button(root,text="Return",command=__menuInit__,fg='#ffffff',bg='#000000').grid(row=0,column=0)
    tkinter.Label(root, text="").grid(row=1,column=0)
    tkinter.Label(root, text="Name: ").grid(row=2,column=0)
    char_name = tkinter.Entry(root)
    char_name.grid(row=2,column=1)
    tkinter.Label(root, text="Class: ").grid(row=3,column=0)
    class_pick = tkinter.OptionMenu(root,c,*charData.classes)
    class_pick.grid(row=3,column=1)
    tkinter.Label(root, text="Weapon: ").grid(row=4,column=0)
    weapon_pick = tkinter.OptionMenu(root,w,*charData.weapons.keys())
    weapon_pick.grid(row=4,column=1)
    tkinter.Label(root, text="Armor: ").grid(row=5,column=0)
    armor_pick = tkinter.OptionMenu(root,a,*charData.armors.keys())
    armor_pick.grid(row=5,column=1)
    
    #Stats - Left Side
    tkinter.Label(root, text="").grid(row=6,column=0)
    tkinter.Label(root, text="Points: ").grid(row=7,column=0)
    points = tkinter.Label(root, text=player.getPoints())
    points.grid(row=7,column=1)
    tkinter.Label(root, text="Strength: ").grid(row=9,column=0)
    stre = tkinter.Label(root, text=player.getStr())
    stre.grid(row=9,column=1)
    tkinter.Button(root, text="Inc", command=lambda:updateStat(stre,"str","+",points)).grid(row=8,column=1)
    tkinter.Button(root, text="Dec", command=lambda:updateStat(stre,"str","-",points)).grid(row=10,column=1)
    tkinter.Label(root, text="Agility: ").grid(row=12,column=0)
    agil = tkinter.Label(root, text=player.getAgi())
    agil.grid(row=12,column=1)
    tkinter.Button(root, text="Inc", command=lambda:updateStat(agil,"agi","+",points)).grid(row=11,column=1)
    tkinter.Button(root, text="Dec", command=lambda:updateStat(agil,"agi","-",points)).grid(row=13,column=1)
    tkinter.Label(root, text="Intelligence: ").grid(row=15,column=0)
    intel = tkinter.Label(root, text=player.getIntel())
    intel.grid(row=15,column=1)
    tkinter.Button(root, text="Inc", command=lambda:updateStat(intel,"intel","+",points)).grid(row=14,column=1)
    tkinter.Button(root, text="Dec", command=lambda:updateStat(intel,"intel","-",points)).grid(row=16,column=1)
    tkinter.Button(root,text="Update",command=lambda:update_char
           (char_name.get(),c.get(),w.get(),a.get(),uName,uHealth,uClass,uWeapon,uArmor,uStr,uAgi,uIntel,w,uDam,uAccu,a,uDodge,uDef),
           fg='#ffffff',bg='#000000').grid(row=17,column=0)
    tkinter.Button(root,text="Play",command=begin,fg='#ffffff',bg='#000000').grid(row=17,column=1)
     
#TODO this is essentially save
def begin():
    f = open(".\chars\player.txt", "w")
    f.writelines(player.getName() + '\n')
    f.writelines(player.getClass() + '\n')
    f.writelines(str(player.getCurrHealth()) + '\n')
    f.writelines(str(player.getMaxHealth()) + '\n')
    f.writelines(player.getWeapon() + '\n')
    f.writelines(str(player.getDamage()) + '\n')
    f.writelines(player.getArmor() + '\n')
    f.writelines(str(player.getDodge()) + '\n')
    f.writelines(str(player.getDefense()) + '\n')
    f.writelines(str(player.getStr()) + '\n')
    f.writelines(str(player.getAgi()) + '\n')
    f.writelines(str(player.getIntel()) + '\n')
    f.writelines(player.getPage())
    f.close()
    loadPage(player.getPage())
    
def loadPage(page):
    clear_screen()
    root.rowconfigure(0,weight=3)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=3)
    root.columnconfigure(2,weight=1)
    f = open(".\pages\\" + page + ".txt", "r")
    flag = f.readline().rstrip()
    check = 0
    if flag != "0":
        #strength check
        if flag == "1":
            check = random.randrange(1,20) + player.getStr()
        #agility check
        elif flag == "2":
            check = random.randrange(1,20) + player.getAgi()
        #intelligence check
        elif flag == "3":
            check = random.randrange(1,20) + player.getIntel()
        if check < int(f.readline().rstrip()):
            newPage = f.readline().rstrip()
            f.close()
            loadPage(newPage)
    else:
        f.readline()
        f.readline()
    tkinter.Label(root, text=f.readline().rstrip()).grid(row=0,column=1)
    opt1=f.readline().rstrip()
    tkinter.Button(root,text=f.readline().rstrip(),command=lambda:loadPage(opt1),fg='#ffffff',bg='#000000').grid(row=1,column=0)
    opt2=f.readline().rstrip()
    tkinter.Button(root,text=f.readline().rstrip(),command=lambda:loadPage(opt2),fg='#ffffff',bg='#000000').grid(row=1,column=2)
    opt3=f.readline().rstrip()
    tkinter.Button(root,text=f.readline().rstrip(),command=lambda:loadPage(opt3),fg='#ffffff',bg='#000000').grid(row=2,column=0)
    opt4=f.readline().rstrip()
    tkinter.Button(root,text=f.readline().rstrip(),command=lambda:loadPage(opt4),fg='#ffffff',bg='#000000').grid(row=2,column=2)
    f.close()
    

#Changes stat number as Inc/Dec buttons pushed
def updateStat(label,stat,mode,points):
    if stat == "str":
        player.updateStat(stat,mode)
        label.config(text=player.getStr())
    elif stat == "agi":
        player.updateStat(stat,mode)
        label.config(text=player.getAgi())
    else:
        player.updateStat(stat,mode)
        label.config(text=player.getIntel())
    points.config(text=player.getPoints())

#Updates right side text with changed values manipulated by player on left
#TODO want to make it to where it will update char values and not have anything
#     to do with label updates 
def update_char(name,spec,weapon,armor,uName,uHealth,uClass,uWeapon,uArmor,uStr,uAgi,uIntel,w,uDam,uAccu,a,uDodge,uDef):
    player.setName(name)
    player.setHealth(spec,0,0)
    player.setClass(spec)
    player.setWeapon(weapon)
    player.setArmor(armor)
    uName.config(text="Name: " + player.getName())
    uClass.config(text="Class: " + player.getClass())
    uHealth.config(text="Health: " + str(player.getMaxHealth()))
    uWeapon.config(text="Weapon: " + player.getWeapon())
    uArmor.config(text="Armor: " + player.getArmor())
    uStr.config(text="Strength: " + str(player.getStr()))
    uAgi.config(text="Agility: " + str(player.getAgi()))
    uIntel.config(text="Intelligence: " + str(player.getIntel()))
    tempDam=charData.weapons[w.get()]
    player.setDamage(tempDam)
    uDam.config(text="Damage Threshold: d" + str(player.getDamage()) + " + " + str(player.getStr()))
    uAccu.config(text="Accuracy: " + str(player.getAgi()))
    tempArmVals=charData.armors[a.get()]
    tempDodge = tempArmVals[0]
    player.setDodge(tempDodge)
    tempDef= tempArmVals[1]
    player.setDefense(tempDef)
    uDodge.config(text="Dodge: " + str(player.getDodge()))
    uDef.config(text="Defense: " + str(player.getDefense()))
    
def load():
    f = open(".\chars\player.txt", "r")
    player.setName(f.readline().rstrip())
    player.setClass(f.readline().rstrip())
    player.setHealth(player.getClass,1,int(f.readline().rstrip()))
    player.setHealth(player.getClass,2,int(f.readline().rstrip()))
    player.setWeapon(f.readline().rstrip())
    player.setDamage(int(f.readline().rstrip()))
    player.setArmor(f.readline().rstrip())
    player.setDodge(int(f.readline().rstrip()))
    player.setDefense(int(f.readline().rstrip()))
    player.setStr(int(f.readline().rstrip()))
    player.setAgi(int(f.readline().rstrip()))
    player.setIntel(int(f.readline().rstrip()))
    player.setPage(f.readline().rstrip())
    f.close()
    loadPage(player.getPage())

def credits():
    clear_screen()
    tkinter.Label(root,text="Programmer: JackAndDraycos",padx=30,pady=30,bg="#555555",font=("Papyrus", 60)).grid(row=0,column=0)
    tkinter.Button(root,text="Return",command=__menuInit__,padx=10,pady=10,fg='#ffffff',bg='#000000').grid(row=1,column=0)

def __menuInit__():
    clear_screen()
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(2,weight=0)
    title = tkinter.Label(root, text="Fantasma",padx=30,pady=30,bg="#555555")
    title.config(font=("Papyrus", 60))

    play_button = tkinter.Button(root, text="Play",command=createChar,padx=10,pady=10,fg='#ffffff',bg='#000000')
    load_button = tkinter.Button(root, text="Load Game", command=load,padx=10,pady=10,fg='#ffffff',bg='#000000')
    credits_button = tkinter.Button(root, text="Credits", command=credits,padx=10,pady=10,fg='#ffffff',bg='#000000')
    exit_button = tkinter.Button(root, text="Quit Game", command=root.quit,padx=10,pady=10,fg='#ffffff',bg='#000000')

    title.grid(row=0,column=0)
    play_button.grid(row=1,column=0)
    load_button.grid(row=2,column=0)
    credits_button.grid(row=3,column=0)
    exit_button.grid(row=4,column=0)

__menuInit__()
root.mainloop()