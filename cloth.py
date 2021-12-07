import time
from particle import Particle
from bar import Bar
import numpy as np
import math as m


class Cloth:
    def __init__(self,jPar,iPar,barTol,partMass):
        self.particles = []
        self.bars = []
        self.violatedBars = []
        self.jPar = jPar
        self.iPar = iPar
        # Creates particles
        nPar = 0
        for i in range(self.iPar):
            tempPar = []
            for j in range(self.jPar):
                    tempPar += [Particle(float(i),float(j),0.0,j == 0,partMass,[i,j])]
                    nPar += 1
            self.particles += [tempPar]
        self.nPart = nPar


        # Create bars
        for i in range(self.iPar):
            for j in range(self.jPar):
                    if(j < self.jPar-1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i][j+1],barTol)]
                    if(j < self.jPar-2):
                        self.bars += [Bar(self.particles[i][j],self.particles[i][j+2],barTol)]


                    if(j < self.jPar-1 and i < self.iPar - 1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+1][j+1],barTol)]
                    if(j < self.jPar-2 and i < self.iPar - 2):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+2][j+2],barTol)]

                    if(i < self.iPar-1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+1][j],barTol)]
                    if(i < self.iPar-2):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+2][j],barTol)]

                    if(j > 0 and i < self.iPar - 1):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+1][j-1],barTol)]
                    if(j > 1 and i < self.iPar - 2):
                        self.bars += [Bar(self.particles[i][j],self.particles[i+2][j-2],barTol)]

                    

    def runSim(self,t):
        self.runVerlet(t)

        it = 0
        while(not self.checkConstraints()):
            it += 1
            
            for vB in self.violatedBars:
                
                self.bars[vB].fix()

            self.violatedBars.clear()
        return it

    def runVerlet(self,t):
        for i in range(self.iPar):
            for j in range(self.jPar):
                self.particles[i][j].verlet(t)
                for bar in self.bars:
                    if(bar.particles[0].index == [i,j]):
                        bar.particles[0] = self.particles[i][j]
                    if(bar.particles[1].index == [i,j]):
                        bar.particles[1] = self.particles[i][j]
    
    def checkConstraints(self):
        check = True
        for i in range(len(self.bars)):
            if(not self.bars[i].checkConstraints()):
                check = False
                self.violatedBars += [i]
        

        return check

    def getVertices(self):
        vertices = []
        for i in range(self.iPar):
            for j in range(self.jPar):
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

    def getNumPar(self):
        return self.nPart

     