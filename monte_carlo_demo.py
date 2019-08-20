# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 02:18:00 2019

@author: Vasco
"""

import random
import turtle

def visualiza(pontos):
    #prepare visualization
    turtle.setworldcoordinates(-3,-3,3,3)
    jan=turtle.Turtle()
    jan.ht()
    jan.speed(0)
    
    #draw square
    jan.up()
    jan.goto(-1,-1)
    jan.down()
    for i in range(4):
        jan.fd(2)
        jan.left(90)
    jan.up()
    
    #draw smaller polygons
    jan.up()
    jan.goto(0,1)
    jan.down()
    jan.goto(0,-1)
    
    jan.up()
    jan.goto(-1,0)
    jan.down()
    jan.goto(0,0)
    jan.goto(1,1)
    jan.up()
    #area of given (above drawn) triangle
    area_triangle = abs(0*(1-1)+0*(1-0)+1*(0-1))/2
    
    #show darts
    for elem in pontos:
        x,y=elem

        #areas of point-made triangles
        tri_1 = abs(0*(1-y)+0*(y-0)+x*(0-1))/2
        tri_2 = abs(0*(y-1)+x*(1-0)+1*(0-y))/2
        tri_3 = abs(x*(1-1)+0*(1-y)+1*(y-1))/2 
        if sum([tri_1, tri_2, tri_3]) == area_triangle or (x < 0 and y < 0):
            jan.color('red')
        else:
            jan.color('green')
        jan.goto(x,y)
        jan.dot()
        
def monte_carlo_pi(num_dardos):
    conta_dardos_dentro=0.0
    tuplos_dardos=tuple()
    #area of given (above drawn) triangle
    area_triangle = abs(0*(1-1)+0*(1-0)+1*(0-1))/2
    
    for i in range(num_dardos):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        tuplos_dardos+=((x,y),)
        
        #areas of point-made triangles
        tri_1 = abs(0*(1-y)+0*(y-0)+x*(0-1))/2
        tri_2 = abs(0*(y-1)+x*(1-0)+1*(0-y))/2
        tri_3 = abs(x*(1-1)+0*(1-y)+1*(y-1))/2     
        if sum([tri_1, tri_2, tri_3]) == area_triangle or (x < 0 and y < 0):
            pass
        else:
            conta_dardos_dentro+=1
    probab = (conta_dardos_dentro/num_dardos)*100
    print('total dots : ',num_dardos)
    print('total green dots : ',conta_dardos_dentro)
    print('probability for random green dot is:', probab)
    return tuplos_dardos

if __name__ == '__main__':
    dardos=monte_carlo_pi(1000)
    visualiza(dardos)
    turtle.exitonclick()
        