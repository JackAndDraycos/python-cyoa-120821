from random import *
from tkinter import *
from charData import *
from functools import partial
root = Tk()
root.title("First Game")
root.geometry("1280x720")
root.option_add("*Font", "Papyrus")

player = creature()

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def play():
    clear_screen()
    root.rowconfigure(0,weight=0)
    root.columnconfigure(0,weight=0)
    root.columnconfigure(2,weight=1)
    c = StringVar()
    c.set(classes[randrange(0,len(classes))])
    w = StringVar()
    w.set(get_stat_name(weapons,1))
    a = StringVar()
    a.set(get_stat_name(armors,(10,0)))

    #Display current stats on right side of page - Initial
    uName=Label(root, text="Name: " + player.getName())
    uName.grid(row=1,column=2)
    uClass=Label(root, text="Class: " + player.getClass())
    uClass.grid(row=2,column=2)
    uHealth=Label(root, text="Health: " + str(player.getHealth()))
    uHealth.grid(row=3,column=2)
    uWeapon=Label(root, text="Weapon: " + player.getWeapon())
    uWeapon.grid(row=4,column=2)
    uAccu=Label(root, text="Accuracy: " + str(player.getAgi()))
    uAccu.grid(row=5,column=2)
    uDam=Label(root, text="Damage Threshold: d" + str(player.getDamage()) + " + " + str(player.getStr()))
    uDam.grid(row=6,column=2)
    uArmor=Label(root, text="Armor: " + player.getArmor())
    uArmor.grid(row=7,column=2)
    #TODO
    uDodge=Label(root, text="Dodge: " + str(player.getDodge()))
    uDodge.grid(row=8,column=2)
    uDef=Label(root, text="Defense: " + str(player.getDefense()))
    uDef.grid(row=9,column=2)
    uStr=Label(root, text="Strength: " + str(player.getStr()))
    uStr.grid(row=10,column=2)
    uAgi=Label(root, text="Agility: " + str(player.getAgi()))
    uAgi.grid(row=11,column=2)
    uIntel=Label(root, text="Intelligence: " + str(player.getIntel()))
    uIntel.grid(row=12,column=2)
    
    #Name entry and drop downs for gear
    Button(root,text="Return",command=__menuInit__,fg='#ffffff',bg='#000000').grid(row=0,column=0)
    Label(root, text="").grid(row=1,column=0)
    Label(root, text="Name: ").grid(row=2,column=0)
    char_name = Entry(root)
    char_name.grid(row=2,column=1)
    Label(root, text="Class: ").grid(row=3,column=0)
    class_pick = OptionMenu(root,c,*classes)
    class_pick.grid(row=3,column=1)
    Label(root, text="Weapon: ").grid(row=4,column=0)
    weapon_pick = OptionMenu(root,w,*weapons.keys())
    weapon_pick.grid(row=4,column=1)
    Label(root, text="Armor: ").grid(row=5,column=0)
    armor_pick = OptionMenu(root,a,*armors.keys())
    armor_pick.grid(row=5,column=1)
    
    #Stats
    Label(root, text="").grid(row=6,column=0)
    Label(root, text="Points: ").grid(row=7,column=0)
    points = Label(root, text=player.getPoints())
    points.grid(row=7,column=1)
    Label(root, text="Strength: ").grid(row=9,column=0)
    stre = Label(root, text=player.getStr())
    stre.grid(row=9,column=1)
    Button(root, text="Inc", command=lambda:updateStat(stre,"str","+",points)).grid(row=8,column=1)
    Button(root, text="Dec", command=lambda:updateStat(stre,"str","-",points)).grid(row=10,column=1)
    Label(root, text="Agility: ").grid(row=12,column=0)
    agil = Label(root, text=player.getAgi())
    agil.grid(row=12,column=1)
    Button(root, text="Inc", command=lambda:updateStat(agil,"agi","+",points)).grid(row=11,column=1)
    Button(root, text="Dec", command=lambda:updateStat(agil,"agi","-",points)).grid(row=13,column=1)
    Label(root, text="Intelligence: ").grid(row=15,column=0)
    intel = Label(root, text=player.getIntel())
    intel.grid(row=15,column=1)
    Button(root, text="Inc", command=lambda:updateStat(intel,"intel","+",points)).grid(row=14,column=1)
    Button(root, text="Dec", command=lambda:updateStat(intel,"intel","-",points)).grid(row=16,column=1)
    Button(root,text="Update",command=lambda:update_char
           (char_name.get(),c.get(),w.get(),a.get(),uName,uHealth,uClass,uWeapon,uArmor,uStr,uAgi,uIntel,w,uDam,uAccu,a,uDodge,uDef),
           fg='#ffffff',bg='#000000').grid(row=17,column=0)
     
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

def update_char(name,spec,weapon,armor,uName,uHealth,uClass,uWeapon,uArmor,uStr,uAgi,uIntel,w,uDam,uAccu,a,uDodge,uDef):
    player.setName(name)
    player.setHealth(spec)
    player.setClass(spec)
    player.setWeapon(weapon)
    player.setArmor(armor)
    uName.config(text="Name: " + player.getName())
    uClass.config(text="Class: " + player.getClass())
    uHealth.config(text="Health: " + str(player.getHealth()))
    uWeapon.config(text="Weapon: " + player.getWeapon())
    uArmor.config(text="Armor: " + player.getArmor())
    uStr.config(text="Strength: " + str(player.getStr()))
    uAgi.config(text="Agility: " + str(player.getAgi()))
    uIntel.config(text="Intelligence: " + str(player.getIntel()))
    tempDam=weapons[w.get()]
    player.setDamage(tempDam)
    uDam.config(text="Damage Threshold: d" + str(player.getDamage()) + " + " + str(player.getStr()))
    uAccu.config(text="Accuracy: " + str(player.getAgi()))
    tempArmVals=armors[a.get()]
    tempDodge = tempArmVals[0]
    player.setDodge(tempDodge)
    tempDef= tempArmVals[1]
    player.setDefense(tempDef)
    uDodge.config(text="Dodge: " + str(player.getDodge()))
    uDef.config(text="Defense: " + str(player.getDefense()))
    
#TODO
def load():
    return

def credits():
    clear_screen()
    Label(root,text="Programmer: JackAndDraycos",padx=30,pady=30,bg="#555555",font=("Papyrus", 60)).grid(row=0,column=0)
    Button(root,text="Return",command=__menuInit__,padx=10,pady=10,fg='#ffffff',bg='#000000').grid(row=1,column=0)

def __menuInit__():
    clear_screen()
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(2,weight=0)
    title = Label(root, text="Fantasma",padx=30,pady=30,bg="#555555")
    title.config(font=("Papyrus", 60))

    play_button = Button(root, text="Play",command=play,padx=10,pady=10,fg='#ffffff',bg='#000000')
    load_button = Button(root, text="Load Game", command=load,padx=10,pady=10,fg='#ffffff',bg='#000000')
    credits_button = Button(root, text="Credits", command=credits,padx=10,pady=10,fg='#ffffff',bg='#000000')
    exit_button = Button(root, text="Quit Game", command=root.quit,padx=10,pady=10,fg='#ffffff',bg='#000000')

    title.grid(row=0,column=0)
    play_button.grid(row=1,column=0)
    load_button.grid(row=2,column=0)
    credits_button.grid(row=3,column=0)
    exit_button.grid(row=4,column=0)

__menuInit__()
root.mainloop()