from cloth import Cloth
import pyvista as pv
import numpy as np

mesh = pv.PolyData()
plotter = pv.Plotter()


c = Cloth(20,10)
vertices = c.getVertices()
faces = c.getFaces()
mesh = pv.PolyData(np.array(vertices),np.array(faces))


plotter.add_mesh(mesh,color='r',show_edges=True,interpolate_before_map = True)
plotter.add_axes()
plotter.enable_eye_dome_lighting()
plotter.show(title="Verlet Cloth", interactive=False, auto_close=False, window_size=[500, 500])
plotter.open_gif("animation.gif")
plotter.write_frame()


for i in range(50):
    c.runSim()
    vertices = c.getVertices()
    plotter.update_coordinates(np.array(vertices), mesh=mesh)
    plotter.write_frame()

