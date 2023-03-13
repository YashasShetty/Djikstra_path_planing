
import numpy as np
import pygame
# 
# Initializing Pygame

openList = []
closedList =[]
pointLists = []
obstacle_color = (0,0,255)
white_color = (255,255,255)
border_color = (150,150,255)
line_color = (255,0,0)
pathpoints = []

pygame.init()


    
# Initializing surface
surface = pygame.display.set_mode((600,250))

def get_pathpoints(i):
    pathpoints.append((openList[i].x,openList[i].y))
    k = i
    while(k>0):
        # print(k)
        print(openList[k].x,openList[k].y)
        k = openList[k].parent_index
        pathpoints.append((openList[k].x,openList[k].y))
        

def find_index_update(new_x,new_y,new_c2c,new_parent_index):
   for l in range(0,len(openList)):
      if openList[l].x == new_x and openList[l].y == new_y:
         if  openList[l].c2c > new_c2c :
            openList[l].c2c = new_c2c
            openList[l].parent_index = new_parent_index


         return True
   return False 

class node:
   def __init__(self, x, y,c2c,new_parent_index):
    self.x = x
    self.y = y
    self.c2c = c2c
    self.index = len(openList)
    self.parent_index = new_parent_index



def create_child(parent_node,horizontal, vertical):
   new_x = parent_node.x + horizontal
   new_y = parent_node.y + vertical
   new_parent_index = parent_node.index
   new_c2c = parent_node.c2c + np.sqrt(vertical**2 + horizontal**2)

   if(find_index_update(new_x,new_y,new_c2c,new_parent_index)):
       pass
   else:
        if 600>new_x>= 0 and 250>new_y >= 0 :
            if surface.get_at((new_x,new_y))!= obstacle_color and surface.get_at((new_x,new_y))!= border_color :
                child = node(new_x,new_y,new_c2c,new_parent_index)
                openList.append(child)
                pointLists.append((new_x,new_y))
                
        else:
            pass

#    if (child.x,child.y) == goal:
#       goal_reached =1
      
   

def move(action_number, parent_node):
    
    if(action_number==1):
        horizontal = 1
        vertical = 0
        
        create_child(parent_node,horizontal,vertical)
        
    elif(action_number==2):
        horizontal = 0
        vertical = 1
        create_child(parent_node,horizontal, vertical)
    elif(action_number==3):
        horizontal = -1
        vertical = 0
        create_child(parent_node,horizontal, vertical)
    elif(action_number==4):
      horizontal = 0
      vertical = -1
      create_child(parent_node,horizontal, vertical)
    elif(action_number==5):
      horizontal = 1
      vertical = 1
      create_child(parent_node,horizontal, vertical)
    elif(action_number==6):
      horizontal = -1
      vertical = 1
      create_child(parent_node,horizontal, vertical)
    elif(action_number==7):
      horizontal = -1
      vertical = -1
      create_child(parent_node,horizontal, vertical)
    elif(action_number==8):
      horizontal = 1
      vertical = -1
      create_child(parent_node,horizontal, vertical)

def if_node_goal(i,goal):
        if(openList[i].x == goal[0] and openList[i].y==goal[1]):
        #    print(openList[i].x,openList[i].y)
           
           return True
        else:
        #    print(goal[0])
        #    print(goal[1])
           return False


def main():

    wrong_coordinates = True
    while wrong_coordinates:
        goal_reached = 0

        goal = (200,50)

        initial = (0,0)
        initial_list =[]
        initial_x = int(input("Enter start x coordinate"))
        initial_list.append(initial_x)
        initial_y = int(input("Enter start y coordinate"))
        initial_list.append(250-initial_y)
        initial = tuple(initial_list)

        goal_list = []
        goal_x = int(input("Enter goal x coordinate"))
        goal_list.append(goal_x)
        goal_y = int(input("Enter goal y coordinate")) 
        goal_list.append(250-goal_y)
        goal = tuple(goal_list)

        wrong_coordinates = False
    
        open_nodes[initial] = (0,0,0)
        child = node(initial[0],initial[1],0,0)
        openList.append(child)
        pointLists.append(initial)
        run = True
        i = 0
        goal_reached = if_node_goal(i,goal)


        

        while run : 
        
        # Initializing Color   
            # current_node = open_nodes.popitem()
            if goal_reached == 0:
                for j in range(1,9):
                    move(j,openList[i])
                    
                
                goal_reached = if_node_goal(i,goal)
                i +=1
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    run =False
                if event.type == pygame.QUIT:
                    run =False
            pygame.display.update()
            # print("start",i)
        

            if goal_reached ==1:             
                    # run =False
                # print(pathpoints)  
                pygame.draw.polygon(surface,white_color , pointLists) 
                if len(pathpoints)== 0 :
                    get_pathpoints(i)
            
                # run = False
            
            

            pygame.draw.polygon(surface,border_color , ((455,10),(455,240),(516.5,125)))
            pygame.draw.polygon(surface,border_color , ((300, 45), (235.04-5*1.7, 85), (235.04 - 5*1.7, 165), (300, 205), (364.95 + 5*1.7, 165), (364.95 +5*1.7, 85)))
            
            pygame.draw.rect(surface, border_color, pygame.Rect(125, 0, 50, 110).inflate(10,1))
            pygame.draw.rect(surface, border_color, pygame.Rect(125, 150, 50, 110).inflate(10,10))
            
            pygame.draw.rect(surface, obstacle_color, pygame.Rect(125, 0, 50, 100))
            pygame.draw.rect(surface, obstacle_color, pygame.Rect(125, 150, 50, 100))
            
            pygame.draw.polygon(surface,obstacle_color , ((460,25),(460,225),(510,125)))
            pygame.draw.polygon(surface,obstacle_color , ((300, 50), (235.04, 87.5), (235.04, 162.5), (300, 200), (364.95, 162.5), (364.95, 87.5)))
            if surface.get_at((initial_x,initial_y))== obstacle_color or surface.get_at((initial_x,initial_x))== border_color :

                print("Start coordinates are in obstacle")
                wrong_coordinates = True
                run = False
            if  surface.get_at((goal_x,goal_y))== obstacle_color or surface.get_at((goal_x,goal_y))== border_color:
                print("Goal coordinates are in obstacle")
                wrong_coordinates = True
                run = False 

            if len(pathpoints)> 0:     
                pygame.draw.lines(surface,line_color,False, pathpoints, 3)
            
            pygame.display.update()



    pygame.quit()
    # print(pathpoints)
    # print(goal[0])
    # print(goal[1])
    # print(pointLists)

main()

