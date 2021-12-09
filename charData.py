class creature:
    def __init__(self,name,spec,weapon,armor):
        self.name = name
        self.spec = spec
        self.weapon = weapon
        self.armor = armor
        if spec == "Warrior":
            self.health = 10
        elif spec == "Rogue":
            self.health = 8
        elif spec == "Mage":
            self.health = 6
        else:
            print("Pick a class")
            
    def update_char(self, name,spec,weapon,armor):
        self.setName(name)
        self.setClass(spec)
        self.setWeapon(weapon)
        self.setArmor(armor)
        print(self.getArmor)
    
    def setName(self, name):
        self.name = name
        
    def setClass(self, spec):
        self.spec = spec
        
    def setWeapon(self, weapon):
        self.weapon = weapon
        
    def setArmor(self, armor):
        self.armor = armor
        
    def getName(self):
        return self.name
        
    def getClass(self):
        return self.spec
        
    def getWeapon(self):
        return self.weapon
        
    def getArmor(self):
        return self.armor
            
classes = (
    'Warrior',
    'Rogue',
    'Mage',
)

#weapon name, damage type
weapons = {
    'Fists':1,
    'Dagger':4,
    'Shortsword':6,
    'Longsword':8,
    'Greatsword':13
}

#armor name, AC(dodge), damage mitigation
armor = {
    'Clothing/Robes':[10,0],
    'Light':[7,3],
    'Medium':[5,5],
    'Heavy':[2,8]
}

#primarily used to set default starting weapon/armor
def get_stat_name(dict, search):
    keys=list(dict.keys())
    values=list(dict.values())
    val_index=values.index(search)
    return keys[val_index]
    