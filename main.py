from cloth import Cloth
import pyvista as pv
import numpy as np

mesh = pv.PolyData()
plotter = pv.Plotter()


c = Cloth(20,10)
vertices = c.getVertices()
faces = c.getFaces()
mesh = pv.PolyData(np.array(vertices),np.array(faces))

plotter.camera_position = [
	(-2.4869290241895983, -4.117635780062769, 261.53798143315186),
 (0.0, 0.0, 250.0),
 (-0.9762657511948513, -0.015644578874755274, -0.21601025483940392)
]
light = pv.Light()
light.set_direction_angle(10, -20)
plotter.add_light(light)
plotter.add_mesh(mesh,color='r',show_edges=True,interpolate_before_map = True,smooth_shading=True)
plotter.add_axes()
plotter.enable_eye_dome_lighting()
plotter.show(title="Verlet Cloth", interactive=False, auto_close=False, window_size=[1000, 500])
plotter.open_gif("animation.gif")
plotter.write_frame()


for i in range(100):
    c.runSim(50.0)
    vertices = c.getVertices()
    # print(len(vertices))
    plotter.update_coordinates(np.array(vertices), mesh=mesh)
    plotter.write_frame()

