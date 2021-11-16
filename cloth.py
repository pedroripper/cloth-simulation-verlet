from particle import Particle
from bar import Bar
import pyvista as pv
from pyvista import demos
import numpy as np
import math as m


class Cloth:
    def __init__(self,jPar,iPar):
        self.particles = []
        self.bars = []
        self.jPar = jPar
        self.iPar = iPar
        self.verticesPar = []
        self.facesPar = []
        # Creates particles
        for i in range(self.iPar):
            tempPar = []
            for j in range(self.jPar):
                    tempPar += [Particle(float(i),float(j),0.0,j == 0,1.0)]
                    # self.verticesPar += tempPar[j]
            self.particles += [tempPar]

        # print(len(self.particles))
        # for i in range(self.jPar):
        #     for j in range(self.iPar):
        #             # print(str(self.particles[i][j].getPos())+" ")
        #     # print("")

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
        
                
    def drawCloth(self):
        vertices = []
        # print(self.particles)
        for i in range(self.iPar):
            for j in range(self.jPar):
                # print(i,j)
                vertices += [self.particles[i][j].getPos()]
            

        faces = []

        # print(vertices)
    # upper triangle faces
        count = 1
        for i in range(len(vertices)-self.jPar-1):
                if(count == self.jPar):
                    count = 1
                    continue
                count += 1
                faces += [[3,i,i+1,i+self.jPar]]
    # lower triangle faces
        count = 1
        for i in range(self.jPar,len(vertices)-1):
            if(count == self.jPar):
                count = 1
                continue
            print(count)
            count += 1
            faces += [[3,i,i-self.jPar+1,i+1]] 
        # faces += [[3,38,38-self.jPar+1,38+1]] 
        
        faces = np.array(faces)
        print(faces)
        vertices = np.array(vertices)
        mesh = pv.PolyData()
        mesh = pv.PolyData(vertices,faces)

        plotter = pv.Plotter()
        plotter.add_mesh(mesh,color='r',show_edges=True,interpolate_before_map = True)
        plotter.add_axes()
        plotter.enable_eye_dome_lighting()
        pl = demos.orientation_plotter()
        pl.camera_position = 'yx'
        plotter.show(interactive=True, auto_close=False, window_size=[800, 600])