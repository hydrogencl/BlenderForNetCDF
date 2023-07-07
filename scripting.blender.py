import bpy
import netCDF4 as NC

from subprocess import run
import os, sys
import math,re

## Import the netCDF from WRF Geo

NC_IN    = NC.Dataset("/Data/Work/PROJECTS/2022.JSC/Visualization/geo_em.d01.nc", "r")

# ============================= 
# example of creating object
# =============================

verts = [ (0,0,0), (0,2,0), (2,2,0), (2,0,0), (1,1,1)]
faces = [ (0,1,4), (0,3,4), (1,2,4),(2,3,4),(0,1,2,3)]

mesh  = bpy.data.meshes.new("Plane")
object = bpy.data.objects.new("Obj", mesh)

bpy.context.collection.objects.link(object)
mesh.from_pydata(verts, [], faces)


# ============================= 
# example of making animation
# =============================

start_pos = (0,0,0)
positions = (0,4,8), (5,4,8), (5,10,8), (9,10,8), (13,10,8),(20,20,20) 
frame_num = 0

for pos in positions:
    bpy.context.scene.frame_set(frame_num)
    object.location = pos
    object.keyframe_insert(data_path="location", index = -1)
    frame_num += 20

# =======================================
# Creating something for the terrain
# =======================================

arr_terrain = [ [1,1,2    ],
                [1,0,3    ],
                [2,3,1    ] ]
                
nx = 3
ny = 3
arr_vert_index = [ [ i+(nx+1)*j for i in range(nx+1)] for j in range(ny+1) ] 
arr_grid_information = []

for j in range(ny):
    for i in range(nx):
        ind_cell = i + j*nx
        arr_grid_information.append(\
        {ind_vertices = [ arr_vert_index[j][i],\
        arr_vert_index[j+1][i],\
        arr_vert_index[j][i+1],\
        arr_vert_index[j+1][i+1] ],
        ind_cell     = ind_grid,
        elevation    = arr_terrain[j][i] 
        })

