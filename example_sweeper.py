
import sweeper 
import pyvista as pv 

plotter = pv.Plotter()

center = [ 
           [[0,0,0], [1,2,0]], 
           [[1,2,0], [5,2,0]], 
           [[5,2,0], [8,8,0]],
           [[8,8,0], [0,8,0]],
           [[0,8,0], [0,0,0]]
           ]

swept = sweeper.sweep_Cylinder(centers=center, radius=0.5, height=1)


center2 = [
           [[12,0,0], [8,2,0]],
           [[8,2,0], [16,5,0]],
           [[16,5,0], [12,8,0]],
           [[12,8,0], [19,18,0]],
           [[19,18,0], [12,0,0]]
           ]
swept2 = sweeper.sweep_Cylinder(centers=center2, radius=0.1, height=0.5) 



plotter.show_grid()
plotter.show_axes()
plotter.add_mesh(swept)
plotter.add_mesh(swept2)
plotter.show()


