import constants as const
import math as math
from particle import Particle
class Bar:
    def __init__(self,l,isHidden,pA,pB):
        self.l = l
        self.isHidden = isHidden
        self.particles = [pA,pB]
        
    def checkConstraints(self):
        if(self.particles[0].distance(self.particles[1].pos) > self.l + 0.005):
            return False
        return True
    

