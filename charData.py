class creature:
    def __init__(self):
        self.name = ""
        self.spec = ""
        self.weapon = "Fists"
        self.armor = "Clothing/Robes"
        self.str = 0
        self.agi = 0
        self.intel = 0
        self.points = 5
        self.currHealth = 0
        self.maxHealth = 0
        self.maxDam = 1
        self.accuracy = 0
        self.dodge = 10
        self.defense = 0
        self.page = "1"
    
    def setName(self, name):
        self.name = name
        
    def setHealth(self,spec,mode,change):
        #init
        if mode == 0:
            if spec == "Warrior":
                self.maxHealth = 10
            elif spec == "Rogue":
                self.maxHealth = 8
            elif spec == "Mage":
                self.maxHealth = 6
            self.maxHealth+=self.str
            self.currHealth = self.maxHealth
        #heal
        elif mode == 1:
            self.currHealth += change
            if self.currHealth > self.maxHealth:
                self.currHealth = self.maxHealth
        #damaged
        else:
            self.currHealth -= change
        
    def setClass(self, spec):
        self.spec = spec
        
    def setWeapon(self, weapon):
        self.weapon = weapon
        
    def setDamage(self, damage):
        self.maxDam = damage
        
    def setArmor(self, armor):
        self.armor = armor
        
    def setDodge(self, dodge):
        self.dodge = dodge
        
    def setDefense(self, defense):
        self.defense = defense
        
    #TODO
    def setPage():
        return
        
    def getName(self):
        return self.name
    
    def getCurrHealth(self):
        return self.currHealth
    
    def getMaxHealth(self):
        return self.maxHealth
        
    def getClass(self):
        return self.spec
        
    def getWeapon(self):
        return self.weapon
    
    def getDamage(self):
        return self.maxDam
        
    def getArmor(self):
        return self.armor
    
    def getDodge(self):
        return self.dodge
    
    def getDefense(self):
        return self.defense
    
    def getPage(self, page):
        return self.page
    
    def updateStat(self,stat,mode):
        if mode == "+":
            if stat == "str":
                if self.str < 5 and self.points > 0:
                    self.str+=1
                    self.points-=1
                    self.maxHealth+=1
            elif stat == "agi":
                if self.agi < 5 and self.points > 0:
                    self.agi+=1
                    self.points-=1
                    self.dodge+=1
            else:
                if self.intel < 5 and self.points > 0:
                    self.intel+=1
                    self.points-=1
        else:
            if stat == "str":
                if self.str > -5:
                    self.str-=1
                    self.points+=1
                    self.maxHealth-=1
            elif stat == "agi":
                if self.agi > -5:
                    self.agi-=1
                    self.points+=1
                    self.dodge-=1
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
    #'Mage', TODO gotta figure out spells but later
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
armors = {
    'Clothing/Robes':(10,0),
    'Light':(7,3),
    'Medium':(5,5),
    'Heavy':(2,8)
}

#primarily used to set default starting weapon/armor, gets key from value
def get_stat_name(dict, search):
    keys=list(dict.keys())
    values=list(dict.values())
    val_index=values.index(search)
    return keys[val_index]