## import necessary module package

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

## import necessary constant

t=(1+(5)**0.5)/2 ##golden ratio
R=((3/2)**0.5)/2 ##radius of a circle 

## define vertices of the shapes

verticies_HEXAHEDRON = (
    (1, -1, -1),    (1, 1, -1),    (-1, 1, -1),    (-1, -1, -1),
    (1, -1, 1),    (1, 1, 1),    (-1, -1, 1),    (-1, 1, 1)
)

verticies_OCTAHEDRON = (
    (0, 1, 0),    (0, 0, -1),    (1, 0, 0),    
    (0, 0, 1),    (-1, 0, 0),    (0, -1, 0)
)

verticies_TETRAHEDRON = (
    (0,0,R),
    (1/(3**0.5),0,(-(2/3)**0.5)/4),
    (-1/2*(3**0.5),1/2,-((2/3)**0.5)/4),
    (-1/2*(3**0.5),-1/2,(-(2/3)**0.5)/4)
)

verticies_DODECAHEDRON = (
    (-1,1,1), ##0
    (0,1/t,t), ##1
    (0,-1/t,t), ##2
    (-1,-1,1), ##3
    (-t,0,1/t), ##4
    (-1/t,-t,0), ##5
    (1/t,-t,0), ##6
    (1,-1,1),  ##7
    (t,0,1/t), ##8
    (1,1,1), ##9
    (1/t,t,0), ##10
    (-1/t,t,0), ##11
    (-1,1,-1), ##12
    (-t,0,-1/t), ##13
    (-1,-1,-1), ##14
    (0,-1/t,-t), ##15
    (0,1/t,-t), ##16
    (1,1,-1), ##17
    (t,0,-1/t), ##18
    (1,-1,-1) ## 19  
)

verticies_ICOSAHEDRON= (
    (0,t,1), #0
    (-1,0,t), #1
    (1,0,t),#2
    (0,-t,1),#3
    (-t,-1,0),#4
    (-t,1,0),#5
    (0,t,-1),#6
    (t,1,0),#7
    (t,-1,0),#8
    (0,-t,-1),#9
    (-1,0,-t),#10
    (1,0,-t) ##11
)

## define the connection between vertices in all shapes

edges_HEXAHEDRON = (
    (0,1),    (0,3),    (0,4),    (2,1),
    (2,3),    (2,7),    (6,3),    (6,4),
    (6,7),    (5,1),    (5,4),    (5,7)
)

edges_OCTAHEDRON = (
    (0,1),    (0,2),    (0,3),    (0,4),
    (5,1),    (5,2),    (5,3),    (5,4),
    (1,2),    (2,3),    (3,4),    (4,1)
)

edges_TETRAHEDRON = (
    (0,1),    (0,2),
    (0,3),    (1,2),
    (2,3),    (3,1)
)

edges_DODECAHEDRON = (
    (0,1),    (0,4),    (0,11),    (1,9),    (1,2), #5
    (2,3),    (2,7),    (3,4),    (3,5),    (4,13), #10
    (5,6),    (5,14),    (6,7),    (6,19),    (7,8), #15
    (8,9),    (8,18),    (9,10),    (10,11),    (10,17), ##20
    (11,12),    (12,13),    (12,16),    (13,14),    (14,15), ##25
    (15,16),    (16,17),    (17,18),    (18,19),    (19,15) ##30
)

edges_ICOSAHEDRON = (
    (0,1),    (0,2),    (0,7),    (0,6),    (0,5), # 5
    (1,2),    (1,3),    (1,4),    (1,5),    (2,3), #10
    (2,8),    (2,7),    (3,4),    (3,9),    (3,8), #15
    (4,5),    (4,10),    (4,9),    (5,6),    (5,10), ##20
    (6,7),    (6,11),    (6,10),    (7,8),    (7,11), ##25
    (8,9),    (8,11),    (9,10),    (9,11),    (10,11) ##30
)

## Create function for each shapes

def HEXAHEDRON():
    glBegin(GL_LINES) 
    for edge in edges_HEXAHEDRON:
        for vertex in edge:
            glVertex3fv(verticies_HEXAHEDRON[vertex]) ## Connecting the vertices command
    glEnd()
            
def OCTAHEDRON():
    glBegin(GL_LINES) 
    for edge in edges_OCTAHEDRON:
        for vertex in edge:
            glVertex3fv(verticies_OCTAHEDRON[vertex]) ## Connecting the vertices command
    glEnd()

def TETRAHEDRON():
    glBegin(GL_LINES)
    for edge in edges_TETRAHEDRON:
        for vertex in edge:
            glVertex3fv(verticies_TETRAHEDRON[vertex]) ## Connecting the vertices command
    glEnd()
    
def DODECAHEDRON():
    glBegin(GL_LINES)
    for edge in edges_DODECAHEDRON:
        for vertex in edge:
            glVertex3fv(verticies_DODECAHEDRON[vertex]) ## Connecting the vertices command
    glEnd()

def ICOSAHEDRON():
    glBegin(GL_LINES) ## inform GL that type of output should be in "line"
    for edge in edges_ICOSAHEDRON:
        for vertex in edge:
            glVertex3fv(verticies_ICOSAHEDRON[vertex]) ## Connecting the vertices command
    glEnd()
    
## Extract the function to create an output through pygame

def main_HEXAHEDRON():
    pygame.init() ## initialisation function to call pygame
    display = (800,600) ##constant
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) ## inform display to specify the usage of openGL

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    ## gluPerspective(field of view, aspect ratio), clipping plane near, clipping plane far)

    glTranslatef(0.0,0.0, -5.0) ## zoom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 1, 1, 0) ## rotating degree
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) ## clear the output between each frame
        HEXAHEDRON() ## Called the cube function
        pygame.display.flip()
        pygame.time.wait(10) #fps 10ms
        
def main_OCTAHEDRON():
    pygame.init() ## initialisation function to call pygame
    display = (800,600) ##constant
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) ## inform display to specify the usage of openGL

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    ## gluPerspective(field of view, aspect ratio), clipping plane near, clipping plane far)

    glTranslatef(0,0, -5.0) ## zoom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 1, 1, 0) ## rotating degree
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) ## clear the output between each frame
        OCTAHEDRON() ## Called the cube function
        pygame.display.flip()
        pygame.time.wait(10) #fps 10ms

def main_TETRAHEDRON():
    pygame.init() ## initialisation function to call pygame
    display = (800,600) ##constant
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) ## inform display to specify the usage of openGL

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    ## gluPerspective(field of view, aspect ratio), clipping plane near, clipping plane far)

    glTranslatef(0,0, -5.0) ## zoom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 1, 1, 0) ## rotating degree
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) ## clear the output between each frame
        TETRAHEDRON() ## Called the cube function
        pygame.display.flip()
        pygame.time.wait(10) #fps 10ms   

def main_DODECAHEDRON():
    pygame.init() ## initialisation function to call pygame
    display = (800,600) ##constant
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) ## inform display to specify the usage of openGL

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    ## gluPerspective(field of view, aspect ratio), clipping plane near, clipping plane far)

    glTranslatef(0.0,0.0, -5.0) ## zoom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 0, 1, 0) ## rotating degree
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) ## clear the output between each frame
        DODECAHEDRON() ## Called the cube function
        pygame.display.flip()
        pygame.time.wait(10) #fps 10ms
        
def main_ICOSAHEDRON():
    pygame.init() ## initialisation function to call pygame
    display = (800,600) ##constant
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) ## inform display to specify the usage of openGL

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    ## gluPerspective(field of view, aspect ratio), clipping plane near, clipping plane far)

    glTranslatef(0.0,0.0, -5.0) ## zoom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 0, 1, 0) ## rotating degree
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) ## clear the output between each frame
        ICOSAHEDRON() ## Called the cube function
        pygame.display.flip()
        pygame.time.wait(10) #fps 10ms


def header():
    print("\n______________________________________________________________________\n")
    print( "\t\t Rotating platonics")
    print("\n______________________________________________________________________\n")

def menu():
    print("\t\t\t Menu")
    print("\t Select the shape that you would like to view \n")
    
    print("\t\t\t 1. HEXAHEDRON ")
    print("\t\t\t 2. OCTAHEDRON ")
    print("\t\t\t 3. TETRAHEDRON ")
    print("\t\t\t 4. DODECAHEDRON ")
    print("\t\t\t 5. ICOSAHEDRON ")
    print("\n\t\t\t 6. EXIT ")
    
    selection = int(input('\n\t\t Your selection : ')) 

    if (selection==6):
        print("\n\t\t Have a good day ! ")
        quit()
    else:
        return selection

def display_shape(selection):
    for x in range(4):
        x=selection

        if x==1:
            print(main_HEXAHEDRON())
        elif (x==2):
            print(main_OCTAHEDRON())
        elif (x==3):
            print(main_TETRAHEDRON())
        elif (x==4):
            print(main_DODECAHEDRON())
        elif (x==5):
            print(main_ICOSAHEDRON())

#Display header banner
header()
# Pass menu choice to varaible
shape_choice = menu()

#User validation loop
while (shape_choice >6):
    print("\n\t SORRY. Your choice is invalid. Please try again.\n")
    shape_choice = menu()

display_shape(shape_choice)
