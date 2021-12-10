class creature:
    def __init__(self,name,spec,weapon,armor,str,agi,intel,points):
        self.name = name
        self.spec = spec
        self.weapon = weapon
        self.armor = armor
        self.str = str
        self.agi = agi
        self.intel = intel
        self.points = points
        if spec == "Warrior":
            self.health = 10
        elif spec == "Rogue":
            self.health = 8
        elif spec == "Mage":
            self.health = 6
    
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
    
    def updateStat(self,stat,mode):
        if mode == "+":
            if stat == "str":
                if self.str < 5 and self.points > 0:
                    self.str+=1
                    self.points-=1
            elif stat == "agi":
                if self.agi < 5 and self.points > 0:
                    self.agi+=1
                    self.points-=1
            else:
                if self.intel < 5 and self.points > 0:
                    self.intel+=1
                    self.points-=1
        else:
            if stat == "str":
                if self.str > -5:
                    self.str-=1
                    self.points+=1
            elif stat == "agi":
                if self.agi > -5:
                    self.agi-=1
                    self.points+=1
            else:
                if self.intel > -5:
                    self.intel-=1
                    self.points+=1
    
    def getStr(self):
        return self.str
        
    def getAgi(self):
        return self.agi
        
    def getIntel(self):
        return self.intel
    
    def getPoints(self):
        return self.points
            
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
    