import pyvista as pv
import numpy as np  


def angleBetweenVectors(vec1, vec2):
  v1 = np.linalg.norm(vec1) 
  v2 = np.linalg.norm(vec2) 
  return np.arccos(np.clip(np.dot(vec1,vec2)/(v1*v2), -1.0, 1.0))  

def distanceBetweenPoints(a, b):
  r =[b[0]-a[0],b[1]-a[1],b[2]-a[2]]
  return np.linalg.norm(r)

def centerPointBetweenPoints(a,b):
  return [(a[0]+b[0])/2, (a[1]+b[1])/2,(a[2]+b[2])/2]

def directionVector(a,b):
  r =[b[0]-a[0],b[1]-a[1],b[2]-a[2]]
  return r/np.linalg.norm(r)



def sweep_Cylinder(centers, radius, height ):

  tool_radius = radius
  tool_diameter = 2*radius
  tool_height = height

  final_sweep = pv.PolyData()

  for center_pair in centers:

    center1 = center_pair[0]
    center2 = center_pair[1]

    direction_nom_vec = directionVector(center1,center2)
    length = distanceBetweenPoints(center1, center2)

    X_rot_angle_cube = np.rad2deg(angleBetweenVectors(direction_nom_vec,[1,0,0]))

    center_cube = centerPointBetweenPoints(center1, center2)
    len_cube = length

    raw_cube = pv.Cube(x_length=len_cube, y_length=tool_diameter, z_length=tool_height, center=center_cube)

    if center2[0]-center1[0]>= 0 and center2[1]-center1[1] >= 0:
      sweep = raw_cube.rotate_z(X_rot_angle_cube, point=center_cube)

    elif center2[0]-center1[0] <= 0 and center2[1]-center1[1] <=0:
      sweep = raw_cube.rotate_z(-X_rot_angle_cube, point=center_cube)
    
    elif center2[0]-center1[0] < 0  and center2[1]-center1[1] >0:
      sweep = raw_cube.rotate_z(X_rot_angle_cube, point=center_cube)

    elif center2[0]-center1[0] > 0  and center2[1]-center1[1] <0:
      sweep = raw_cube.rotate_z(-X_rot_angle_cube, point=center_cube)

    

  
    vistaMesh1 = pv.Cylinder(center=center1, radius= tool_radius, height= tool_height, direction=(0,0,1))
    vistaMesh2 = pv.Cylinder(center=center2, radius= tool_radius, height= tool_height, direction=(0,0,1))

    sweep.merge([vistaMesh1, vistaMesh2], inplace=True)
    final_sweep.merge(sweep, inplace=True)

  return final_sweep

  
