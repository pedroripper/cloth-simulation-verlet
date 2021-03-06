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
        sum_ = 0
        pos = self.getPos()
        for i in range(len(pos)):
            sum_ += (pos[i]-vec2[i])*(pos[i]-vec2[i])
        return m.sqrt(sum_)
    
    def subtract(self, vec2):
        x2 = (self.x-vec2[0])
        y2 = (self.y-vec2[1])
        z2 = (self.z-vec2[2])    
        return Vector3d(x2,y2,z2)
    
    def add(self, vec2):
        x2 = (self.x+vec2[0])
        y2 = (self.y+vec2[1])
        z2 = (self.z+vec2[2])    
        return Vector3d(x2,y2,z2)

    def module(self):
        sum_ = 0
        for val in self.getPos():
            sum_ += val*val
        return m.sqrt(sum_)

    def unitary(self):
        module = self.module()
        if(module == 0):
            return self
        x2 = (self.x)/module
        y2 = (self.y)/module
        z2 = (self.z)/module
        return Vector3d(x2,y2,z2)

    def multiply(self,f):
        x2 = (self.x)*f
        y2 = (self.y)*f
        z2 = (self.z)*f
        return Vector3d(x2,y2,z2)

    def divide(self,f):
        x2 = (self.x)/f
        y2 = (self.y)/f
        z2 = (self.z)/f
        return Vector3d(x2,y2,z2)

