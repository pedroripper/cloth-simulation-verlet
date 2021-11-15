import constants as const
import math as math
class particle:
    def __init__(self,x,y,z,isFixed,mass):
        self.x = x
        self.y = y
        self.z = z
        self.xp = x
        self.yp = y
        self.zp = z
        self.isFixed = isFixed
        self.m = mass

    def gravity(self,axis):
        if(self.isFixed):
            return 0.0
        return const.g[axis]*self.m
    def wind(self,axis,t):
        if(self.isFixed):
            return 0.0
        return const.w*math.exp(-t/20.0)
    def totalForce(self,t,axis):
        return self.gravity(axis)+self.wind(axis,t)
    
    def verlet(self,t,h):
        tempx = self.x
        tempy = self.y
        tempz = self.z
        self.x = self.x + (1-const.amort)*(self.x-self.xp) + h*h*(self.totalForce(t,0))/self.m;
        self.y = self.y + (1-const.amort)*(self.y-self.yp) + h*h*(self.totalForce(t,1))/self.m;
        self.z = self.z + (1-const.amort)*(self.z-self.zp) + h*h*(self.totalForce(t,2))/self.m;
        self.xp = tempx
        self.yp = tempy
        self.zp = tempz
    
    def getPos(self):
        return [self.x,self.y,self.z]


