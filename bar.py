from re import I
import constants as const
import math as m
from particle import Particle

from vec3d import Vector3d
import time
class Bar:
    def __init__(self,pA,pB):
        self.particles = [pA,pB]
        self.l = pA.distance(pB)



    def checkConstraints(self):
        distance = self.particles[0].distance(self.particles[1])
        if(distance > (self.l + 0.005)):            
            return False
        return True
    
    def fix(self):

        v1 = self.particles[0].getVec()

        v2 = self.particles[1].getVec()

        vdist = v1.subtract(v2.getPos())
        
        vLength = vdist.module()

        unit = vdist.divide(vLength)

        dif = vLength - self.l

        
        if(self.particles[0].isFixed and not(self.particles[1].isFixed)):
            movePos = unit.multiply(dif)
            self.particles[1].move(movePos)

        if(not(self.particles[0].isFixed) and self.particles[1].isFixed):
            movePos = unit.multiply(-dif)
            self.particles[0].move(movePos)
        else:
            movePosNeg = unit.multiply(-dif/2)
            self.particles[0].move(movePosNeg)
            movePosPos = unit.multiply(dif/2)

            self.particles[1].move(movePosPos)
    