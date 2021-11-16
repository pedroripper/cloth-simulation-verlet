# sphinx_gallery_thumbnail_number = 2
import pyvista as pv

import numpy as np




vertices = np.array([[0, 0, 0],
                     [1, 0, 1],
                     [0, 1, 0],
                     [1, 1, 0],
                     [0.5,0,1]
                     ])

# mesh faces
faces = np.hstack([[2,0,1],
                   [2,0,2]

                   ])    # triangle


# pv.global_theme.load_theme(my_theme)

mesh = pv.PolyData(vertices,faces)

plotter = pv.Plotter()
plotter.add_mesh(mesh,color='r',show_edges=False,interpolate_before_map = True)
plotter.add_axes()
plotter.enable_eye_dome_lighting()
plotter.show(interactive=True, auto_close=False, window_size=[800, 600])

# plot each face with a different color

# surf.plot(scalars=np.arange(2), cpos=[-1, 1, 0.5],theme)