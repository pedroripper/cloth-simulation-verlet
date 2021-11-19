import time
from particle import Particle
from bar import Bar
import numpy as np
import math as m


class Cloth:
    def __init__(self,jPar,iPar):
        self.particles = []
        self.bars = []
        self.violatedBars = []
        self.jPar = jPar
        self.iPar = iPar
        # Creates particles
        for i in range(self.iPar):
            tempPar = []
            for j in range(self.jPar):
                    tempPar += [Particle(float(i)*10.0,float(j)*10.0,0.0,j == 0,5.0,[i,j])]
            self.particles += [tempPar]

        # Create bars
        for i in range(self.iPar):
            for j in range(self.jPar):
                    if(j < self.jPar-1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i][j+1])]
                    if(j < self.jPar-1 and i < self.iPar - 1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+1][j+1])]
                    if(i < self.iPar-1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+1][j])]
                    if(j > 0 and i < self.iPar - 1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+1][j-1])]
        self.bars += [Bar(self.particles[0][0],self.particles[self.iPar-1][self.jPar-1])]
        self.bars += [Bar(self.particles[0][0],self.particles[0][self.jPar-1])]
        self.bars += [Bar(self.particles[0][0],self.particles[self.iPar-1][0])]
        self.bars += [Bar(self.particles[self.iPar-1][0],self.particles[self.iPar-1][self.jPar-1])]
        self.bars += [Bar(self.particles[self.iPar-1][0],self.particles[0][self.jPar-1])]
        self.bars += [Bar(self.particles[0][self.jPar-1],self.particles[self.iPar-1][self.jPar-1])]
    


    def runVerlet(self,t):

        for i in range(self.iPar):
            for j in range(self.jPar):
                self.particles[i][j].verlet(t)
                for bar in self.bars:
                    if(bar.particles[0].index == [i,j]):
                        bar.particles[0] = self.particles[i][j]
                    if(bar.particles[1].index == [i,j]):
                        bar.particles[1] = self.particles[i][j]
        

    def getVertices(self):
        vertices = []
        # print(self.particles)
        for i in range(self.iPar):
            for j in range(self.jPar):
                # print(i,j)
                vertices += [self.particles[i][j].getPos()]
        return vertices
    

    def getFaces(self):
        faces = []
    # upper triangle self.faces
        count = 1
        for i in range(self.iPar*self.jPar-self.jPar-1):
                if(count == self.jPar):
                    count = 1
                    continue
                count += 1
                faces += [[3,i,i+1,i+self.jPar]]
    # lower triangle self.faces
        count = 1
        for i in range(self.jPar,self.iPar*self.jPar-1):
            if(count == self.jPar):
                count = 1
                continue
            count += 1
            faces += [[3,i,i-self.jPar+1,i+1]] 

        return faces


    
    def checkConstraints(self):
        check = True
        for i in range(len(self.bars)):
            if(not self.bars[i].checkConstraints()):
                check = False
                self.violatedBars += [i]
        

        return check
    
    def runSim(self,t):

        # print("Rodando")

        self.runVerlet(t)
       




        while(not self.checkConstraints()):

            
            for vB in self.violatedBars:
                
                self.bars[vB].fix()

            self.violatedBars.clear()
            

     