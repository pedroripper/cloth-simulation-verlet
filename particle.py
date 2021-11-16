import constants as const
import math as math
from vec3d import Vector3d
class Particle:
    def __init__(self,x,y,z,isFixed,mass):
        self.pos = Vector3d(x,y,z)
        self.posp = Vector3d(x,y,z)
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
        cPosition = self.pos.getPos()
        tPosition = cPosition
        cPosition[0] = cPosition[0] + (1-const.amort)*(cPosition[0]-tPosition[0]) + h*h*(self.totalForce(t,0))/self.m;
        cPosition[1] = cPosition[1] + (1-const.amort)*(cPosition[1]-tPosition[1]) + h*h*(self.totalForce(t,1))/self.m;
        cPosition[2] = cPosition[2] + (1-const.amort)*(cPosition[2]-tPosition[2]) + h*h*(self.totalForce(t,2))/self.m;
        self.posp.updatePos(tPosition)
        self.pos.updatePos(cPosition)

    def move(self,delta,axis):
        if(self.isFixed):
            return
       
    def getPos(self):
        return self.pos.getPos()

    def distance(self,pB):
        return self.pos.distance(pB.pos)


