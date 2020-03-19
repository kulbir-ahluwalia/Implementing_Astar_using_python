# -*- coding: utf-8 -*-
"""action_set.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AUVzpTgNkU4F5IxtjvT2kH8OQk_wFqSi
"""

import numpy as np
import math
import obstacle_map


def load_map(fname = None):
    if fname is not None :
        map_ = cv2.imread(fname)
        return map_
    world= 255*np.ones((200,300,3))
    rc=0
    obstacle_map.obstacle_circle(world)
    obstacle_map.obstacle_ellipse(world)
    obstacle_map.obstacle_rhombus(world)
    obstacle_map.obstacle_rectangle(world)
    obstacle_map.obstacle_polygon(world)

    cv2.imwrite('./map.jpg',world)
    return world


def isValidNode(map_,x,y,rad):
    rows,cols = map_.shape[:2]
    if 0 <= x-rad and x+rad < rows and 0 <= y-rad and y+rad < cols:
        if not detectCollision(map_, (x,y), rad):
            return True
        else :
            return False
    else:
        return False


def detectCollision(img, center,radius):
    for i in range(2*radius+1):
        for j in range(2*radius+1):
            if i**2+j**2 <= radius**2:
                if not ((img[int(center[0])+i][int(center[1])+j]==(255,255,255)).all() and (img[int(center[0])+i][int(center[1])-j]==(255,255,255)).all()\
                        and (img[int(center[0])-i][int(center[1])-j]==(255,255,255)).all() and (img[int(center[0])-i][int(center[1])+j]==(255,255,255)).all()):
                    return True
    return False


def heu(node1, node2):
  dist= math.sqrt( (node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)
  return dist


def move_along(node):
  temp= [0,0,0]
  angle = math.radians(node[2]+ 0)
  temp[0] = node[0] + 0.5* math.cos(angle)
  temp[1] = node[1] + 0.5* math.sin(angle)
  temp[2] = node[2]+0
  return temp

def move_UP1(node):
  temp= [0,0,0]
  angle = math.radians(node[2]+ 30)
  temp[0] = node[0] + 0.5* math.cos(angle)
  temp[1] = node[1] + 0.5* math.sin(angle)
  temp[2] = node[2]+ 30
  return temp
  
def move_UP2(node):
  temp= [0,0,0]
  angle = math.radians(node[2]+ 60)
  temp[0] = node[0] + 0.5* math.cos(angle)
  temp[1] = node[1] + 0.5* math.sin(angle)
  temp[2] = node[2]+ 60
  return temp

def move_DN1(node):
  temp= [0,0,0]
  angle = math.radians(node[2]- 30)
  temp[0] = node[0] + 0.5* math.cos(angle)
  temp[1] = node[1] + 0.5* math.sin(angle)
  temp[2] = node[2] -30
  return temp

def move_DN2(node):
  temp= [0,0,0]
  angle = math.radians(node[2]- 60)
  temp[0] = node[0] + 0.5* math.cos(angle)
  temp[1] = node[1] + 0.5* math.sin(angle)
  temp[2] = node[2] -60
  return temp


def generate_child(node):
  child= []
  child.append(node)
  parent= []
  i=0
  
  nd = move_along(child[i])
  x =nd[0]
  y= nd[1]
  if isValidNode(map_, x, y, rad):
    if nd not in child:
        child.append(nd)
        

  nd= move_UP1(child[i])
  x =nd[0]
  y= nd[1]
  if isValidNode(map_, x, y, rad):
    if nd not in child:
        child.append(nd)
        

  nd = move_UP2(child[i])
  x =nd[0]
  y= nd[1]
  if isValidNode(map_, x, y, rad):
    if nd not in child:
        child.append(nd)
        

  nd = move_DN1(child[i])
  x =nd[0]
  y= nd[1]
  if isValidNode(map_, x, y, rad):
    if nd not in child:
        child.append(nd)

  nd = move_DN2(child[i])
  x =nd[0]
  y= nd[1]
  if isValidNode(map_, x, y, rad):
    if nd not in child:
        child.append(nd)
        
  parent.append(child[i])
  return child, parent


map_=load_map()
rows, cols = map_.shape[:2]

print("Enter the start node co-ordinates")
startx= int(input("x is: "))
starty= int(input("y is: "))

# print("Enter the goal node co-ordinates")
# goalx= int(input("x is: "))
# goaly= int(input("y is: "))

print("Enter the initial angle for the robot:  ")
theta_i = int(input("theta_i is: "))

print("Enter the robot parameters:")
rad = int(input("Enter the radius of the robot: "))
clr = int(input("Enter the robot clearance: "))

#starty= rows-starty-1
#goaly= rows-goaly-1

start=[startx, starty, theta_i]
#goal= [goalx, goaly]

child, parent = generate_child(start)
print(child)