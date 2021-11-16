import math as m

class Vector3d:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def getPos(self):
        return [self.x,self.y,self.z]

    def updatePos(self,newPos):
        self.x = newPos[0]
        self.y = newPos[1]
        self.z = newPos[2]
    
    def distance(self,vec2):
        x2 = (self.x-vec2.x)**2
        y2 = (self.y-vec2.y)**2
        z2 = (self.z-vec2.z)**2
        return m.sqrt(x2+y2+z2)