import constants as const
import math as math
from vec3d import Vector3d
import time

class Particle:
    def __init__(self,x,y,z,isFixed,mass,index):
        self.pos = Vector3d(x,y,z)
        self.lastPos = Vector3d(x,y,z)
        self.isFixed = isFixed
        self.m = mass
        self.index = index

    def gravity(self,axis):
        if(self.isFixed):
            return 0.0
        return const.g[axis]*self.m
    def wind(self,axis,t):
        if(self.isFixed):
            return 0.0
        return const.w[axis]*math.exp(-t/20.0)
    def totalForce(self,t,axis):
        return self.gravity(axis)+self.wind(axis,t)
    
    def verlet(self,t):

        cPosition = self.pos.getPos()
        lPosition = self.lastPos.getPos()
        tPosition = cPosition       

        cPosition[0] = cPosition[0] + (1.0-const.amort)*(cPosition[0]-lPosition[0]) + (t/1000.0)*(t/1000.0)*(self.totalForce(t,0))/self.m;
        cPosition[1] = cPosition[1] + (1.0-const.amort)*(cPosition[1]-lPosition[1]) + (t/1000.0)*(t/1000.0)*(self.totalForce(t,1))/self.m;
        cPosition[2] = cPosition[2] + (1.0-const.amort)*(cPosition[2]-lPosition[2]) + (t/1000.0)*(t/1000.0)*(self.totalForce(t,2))/self.m;

        newPos = Vector3d(cPosition[0],cPosition[1],cPosition[2])

        self.updatePos(self.pos,newPos)



    def updatePos(self,current,new):
        self.lastPos = current
        self.pos = new
        
    def move(self,distV):
        if(self.isFixed):
            return
        else:
            newPos = self.pos.add(distV.getPos())
            self.pos = newPos
            
    def getPos(self):
        return self.pos.getPos()

    def getLastPos(self):
        return self.lastPos.getPos()
    
    def getVec(self):
        return self.pos

    def distance(self,pB):
        return self.pos.distance(pB.getPos())


