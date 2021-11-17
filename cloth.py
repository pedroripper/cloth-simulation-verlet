from particle import Particle
from bar import Bar
import numpy as np
import math as m


class Cloth:
    def __init__(self,jPar,iPar):
        self.particles = []
        self.bars = []
        self.jPar = jPar
        self.iPar = iPar
        # Creates particles
        for i in range(self.iPar):
            tempPar = []
            for j in range(self.jPar):
                    tempPar += [Particle(float(i)*10.0,float(j)*10.0,0.0,j == 0,1.0)]
            self.particles += [tempPar]

        # Create bars
        for i in range(self.iPar):
            for j in range(self.jPar):
                    if(j<self.jPar-1):
                        self.bars += [Bar(10.0,False,self.particles[i][j],self.particles[i][j+1])] 
                    if(i<self.iPar-1):
                        self.bars += [Bar(10.0,False,self.particles[i][j],self.particles[i+1][j])]
                    if(i<self.iPar-1 and j<self.jPar-1):
                        self.bars += [Bar(10.0,False,self.particles[i][j],self.particles[i+1][j+1])] 
                    if(j>0 and j <self.jPar-1 and i < self.iPar-1):
                        self.bars += [Bar(10.0*m.sqrt(2.0),False,self.particles[i][j],self.particles[i+1][j-1])]


    def runVerlet(self):
        for i in range(self.iPar):
            for j in range(self.jPar):
                self.particles[i][j].verlet(5.0,0.1)
        

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
        for bar in self.bars:
            if(bar.checkConstraints()):
                check = False
                
        return check
    
    def runSim(self):
        self.runVerlet()
        # corrigir o tamanho das barras


        # for i in range(self.iPar):
        #     for j in range(self.jPar):
        #         print(self.particles[i][j].getPos())