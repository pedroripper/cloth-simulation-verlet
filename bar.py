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
        # print("Faz o favor ", distance)
        # if(distance > 100):
        #     # exit()
        if(distance > (self.l + 0.005)):
            # print(" OLHA PQ NAO FAZ ", self.l)
            
            return False
        return True
    
    def fix(self):
        
        
        # if(self.particles[1].index == [1,1]):
        #     print("Ao entrar no fix 0,0 tava assim:", self.particles[0].getPos())
        #     print("Ao entrar no fix 1,1 tava assim:", self.particles[1].getPos())



        v1 = self.particles[0].getVec()

        v2 = self.particles[1].getVec()
        # if(self.particles[1].index == [1,1] and self.particles[0].index == [0,0]):

        #     print("V1",  v1.getPos())
        #     print("V2",  v2.getPos())


        vdist = v1.subtract(v2.getPos())
        # print("VDIST ", vdist.getPos())
        
        vLength = vdist.module()
        # print(vLength)

        

        unit = vdist.divide(vLength)
        # print(unit.getPos())


        dif = vLength - self.l
        # print("Diferenca: ", dif)

        
        if(self.particles[0].isFixed and not(self.particles[1].isFixed)):
            movePos = unit.multiply(dif)
            # print("O que deveria mover", movePos.getPos())
            # print("Logo antes de mover", self.particles[1].getPos())
            self.particles[1].move(movePos)
            # print("Logo depois de mover", self.particles[1].getPos())
            # exit()
        if(not(self.particles[0].isFixed) and self.particles[1].isFixed):
            movePos = unit.multiply(-dif)
            self.particles[0].move(movePos)
        else:
            movePosNeg = unit.multiply(-dif/2)
            self.particles[0].move(movePosNeg)
            movePosPos = unit.multiply(dif/2)
            # print("----->", movePosPos.getPos())
            self.particles[1].move(movePosPos)
        # if(self.particles[1].index == [1,0]):
        #     # print("Depois tava assim:", self.particles[1].getPos())
        #     exit()
        

        # time.sleep(5)
        
            

        # # print("Distancia inicial:", vLength)

        # dif = vLength - self.l

        # unitV = vdist.divide(vLength)
        # # print(unitV.getPos())

        
        # if(self.particles[0].isFixed or self.particles[1].isFixed):

        #     toMoveDoublePos = unitV.multiply(dif)
        #     toMoveDoubleNeg = unitV.multiply(-dif)
        #     self.particles[0].move(toMoveDoubleNeg)
        #     self.particles[1].move(toMoveDoublePos)
        # else:
        #     toMovePos = unitV.multiply(dif/2.0)
        #     toMoveNeg = unitV.multiply(-dif/2.0)
        #     self.particles[0].move(toMoveNeg)
        #     self.particles[1].move(toMovePos)

        # v1 = self.particles[0].getVec()
        # v2 = self.particles[1].getVec()
       
        # vdist = v1.subtract(v2.getPos())

        # vLength = vdist.module()
        
        # print("Distancia final:", vLength)
        # print("V1_> ", v1.getPos())
        # print("V2_> ", v2.getPos())

        # distance = self.particles[0].distance(self.particles[1])
        # dif = abs(self.l-distance)
        # vec = self.particles[0].pos.subtract(self.particles[1].getPos())
        # unitVec = vec.unitary()
        # if(self.particles[0].isFixed or self.particles[1].isFixed):
        #     m1 = unitVec.multiply(-dif)
        #     m2 = unitVec.multiply(dif)
        #     self.particles[0].move(m1.getPos())
        #     self.particles[1].move(m2.getPos())
        # else:
        #     m1 = unitVec.multiply(-dif/2)
        #     m2 = unitVec.multiply(dif/2)
        #     self.particles[0].move(m1.getPos())
        #     self.particles[1].move(m2.getPos())
        # print(self.particles[0].distance(self.particles[1]))
