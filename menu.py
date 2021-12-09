from random import *
from tkinter import *
from charData import *
from functools import partial
root = Tk()
root.title("First Game")
root.geometry("1280x720")
root.option_add("*Font", "Papyrus")

player = creature("","","Fists","Clothing/Robes")

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def play():
    clear_screen()
    root.rowconfigure(0,weight=0)
    root.columnconfigure(0,weight=0)
    root.columnconfigure(2,weight=1)
    uName=Label(root, text="Name: " + player.getName())
    uName.grid(row=1,column=2)
    uClass=Label(root, text="Class: " + player.getClass())
    uClass.grid(row=2,column=2)
    uWeapon=Label(root, text="Weapon: " + player.getWeapon())
    uWeapon.grid(row=3,column=2)
    uArmor=Label(root, text="Armor: " + player.getArmor())
    uArmor.grid(row=4,column=2)
    Button(root,text="Return",command=__menuInit__,fg='#ffffff',bg='#000000').grid(row=0,column=0)
    Label(root, text="").grid(row=1,column=0)
    Label(root, text="Name: ").grid(row=2,column=0)
    char_name = Entry(root)
    char_name.grid(row=2,column=1)
    c = StringVar()
    c.set(classes[randrange(0,len(classes))])
    w = StringVar()
    w.set(get_stat_name(weapons,1))
    a = StringVar()
    a.set(get_stat_name(armor,[10,0]))
    Label(root, text="Class: ").grid(row=3,column=0)
    class_pick = OptionMenu(root,c,*classes)
    class_pick.grid(row=3,column=1)
    Label(root, text="Weapon: ").grid(row=4,column=0)
    weapon_pick = OptionMenu(root,w,*weapons)
    weapon_pick.grid(row=4,column=1)
    Label(root, text="Armor: ").grid(row=5,column=0)
    armor_pick = OptionMenu(root,a,*armor)
    armor_pick.grid(row=5,column=1)
    
    Label(root, text="").grid(row=6,column=0)
    Label(root, text="Strength: ").grid(row=8,column=0)
    Label(root, text=0).grid(row=8,column=1)
    Button(root, text="Inc").grid(row=7,column=1)
    Button(root, text="Dec").grid(row=9,column=1)
    Label(root, text="Agility: ").grid(row=11,column=0)
    Label(root, text=0).grid(row=11,column=1)
    Button(root, text="Inc").grid(row=10,column=1)
    Button(root, text="Dec").grid(row=12,column=1)
    Label(root, text="Intelligence: ").grid(row=14,column=0)
    Label(root, text=0).grid(row=14,column=1)
    Button(root, text="Inc").grid(row=13,column=1)
    Button(root, text="Dec").grid(row=15,column=1)
    Button(root,text="Update",command=lambda:update_char(char_name.get(),c.get(),w.get(),a.get(),uName,uClass,uWeapon,uArmor),fg='#ffffff',bg='#000000').grid(row=17,column=0)
    
def update_char(name,spec,weapon,armor,uName,uClass,uWeapon,uArmor):
    player.setName(name)
    player.setClass(spec)
    player.setWeapon(weapon)
    player.setArmor(armor)
    uName.config(text="Name: " + player.getName())
    uClass.config(text="Class: " + player.getClass())
    uWeapon.config(text="Weapon: " + player.getWeapon())
    uArmor.config(text="Armor: " + player.getArmor())
    
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