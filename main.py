from cloth import Cloth
import pyvista as pv

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

mesh = pv.PolyData()
plotter = pv.Plotter()




c = Cloth(15,10)
vertices = c.getVertices()
faces = c.getFaces()
mesh = pv.PolyData(np.array(vertices),np.array(faces))

plotter.camera_position = [
(4.5920040953099255, 2.427775565730334, 45.46159577341813),
 (10.0, 10.0, -20.0),
 (-0.9758831176030498, 0.01636214830833893, -0.2176796289965784)
]


# 	(0,15,80),
#  (10, 4, -20.0),
#  (0,0,0)

# plotter.camera.roll -= 90

# plotter.camera.roll += 100
light = pv.Light(position=(-10, 0, 0),
                       focal_point=(10, 15, 0),
                       color=[1, 1.0, 0.9843, 1],  # Color temp. 5400 K
                       intensity=2.3)
plotter.add_light(light)


plotter.add_mesh(mesh,show_edges=False,interpolate_before_map = True,smooth_shading=True,color='r')
plotter.add_axes()
plotter.enable_eye_dome_lighting()
plotter.show(title="Verlet Cloth", interactive=False, auto_close=False, window_size=[1000, 1000])
plotter.open_gif("animation.gif")
plotter.write_frame()


for i in range(150):
    print("Iteração ", i+1)
    print(plotter.camera_position)
    c.runSim(5.0)
    vertices = c.getVertices()
    # print(len(vertices))
    plotter.update_coordinates(np.array(vertices), mesh=mesh)
    plotter.camera.reset_clipping_range()
    plotter.write_frame()

