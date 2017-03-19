#File: USFlag.py
#Description: Program creates US flag given an input of flag height in pixels.
#Student's Name: Andrew Chou
#Student's UT EID: aoc349
#Course Name: CS 313E 
#Unique Number: 50940
#
# Date Created: 9/9/16
# Date Last Modified: 9/16/16


#function draws in stripes of US flag
def drawStripes(x, y, height, width, ttl):
    
    ttl.speed(10)
    
    ttl.up()
    
    start_x = x
    start_y = y
    
    for i in range(7):
        
        ttl.fillcolor("red")
        ttl.goto(start_x, start_y)
        ttl.begin_fill()
        ttl.down()
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.left(90)
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.end_fill()
        ttl.left(90)
        ttl.up()
        start_y += 2 * height
        ttl.down()
    
    ttl.up()
    ttl.goto(x + width, y)
    ttl.down()
    ttl.goto(x + width, y + 13 * height)
    ttl.up()
      
      
#function draws canton of US flag
def drawCanton(x, y, canton_height, canton_width, flag_height, ttl):  
      
      ttl.speed(10)
      
      ttl.up()
      
      ttl.fillcolor("blue")
      ttl.goto(x, y + flag_height)
      ttl.down()
      ttl.begin_fill()
      
      for i in range(2):
        ttl.forward(canton_width)
        ttl.right(90)
        ttl.forward(canton_height)
        ttl.right(90)
      
      ttl.end_fill()


  
#function draws stars of US flag
def drawStars(x, y, radius, ttl, colWidth, rowWidth):
    
    ttl.speed(10)
    ttl.up()
    ttl.goto(x,y)
    
    new_y1 = y
    
    y_inner = y + .7 * radius
    
    inner_radius = .35 * radius
    
    #draws rows 1, 3, 5, 7, and 9
    for i in range(5):
        for j in range(6):

            #outer vertices of star
            a1 = ttl.position()
            ttl.circle(radius, 45)
            a2 = ttl.position()
            ttl.circle(radius, 65)
            a3 = ttl.position()
            ttl.circle(radius, 70)
            a4 = ttl.position()
            ttl.circle(radius, 70)
            a5 = ttl.position()
            ttl.circle(radius, 65)
            a6 = ttl.position()
            ttl.circle(radius, 45)
            
            ttl.seth(0)
            
            #inner vertices of star
            
            ttl.sety(y_inner) 
            
            b1 = ttl.position()
            ttl.circle(inner_radius, 72)
            b2 = ttl.position()
            ttl.circle(inner_radius, 72)
            b3 = ttl.position()
            ttl.circle(inner_radius, 72)
            b4 = ttl.position()
            ttl.circle(inner_radius, 72)
            b5 = ttl.position()
            ttl.circle(inner_radius, 72)
            b6 = ttl.position()
            
            ttl.seth(0)
            
            
            #connect vertices to make star
            ttl.fillcolor("white")
            
            ttl.goto(a2)
            ttl.down()
            
            ttl.begin_fill()
            ttl.goto(b2)
            ttl.goto(a3)
            ttl.goto(b3)
            ttl.goto(a4)
            ttl.goto(b4)
            ttl.goto(a5)
            ttl.goto(b5)
            ttl.goto(a6)
            ttl.goto(b1)
            ttl.goto(a2)
            ttl.end_fill()
            
            ttl.up()
            ttl.goto(a1)
            ttl.seth(0)
            
            
            ttl.forward(2 * colWidth)
            
            

        new_y1 -= 2 * rowWidth
        y_inner = new_y1 + .7 * radius
        ttl.goto(x, new_y1)
    
    
    #draws rows 2, 4, 6, and 8
    new_x = x + colWidth
    new_y2 = y - rowWidth
    y_inner = new_y2 + .7 * radius
    
    ttl.goto(new_x, new_y2)
    ttl.seth(0)
    for i in range(4):
        for j in range(5):

            #outer vertices of star
            c1 = ttl.position()
            ttl.circle(radius, 45)
            c2 = ttl.position()
            ttl.circle(radius, 65)
            c3 = ttl.position()
            ttl.circle(radius, 70)
            c4 = ttl.position()
            ttl.circle(radius, 70)
            c5 = ttl.position()
            ttl.circle(radius, 65)
            c6 = ttl.position()
            ttl.circle(radius, 45)
            
            ttl.seth(0)
            
            #inner vertices of star
            
            ttl.sety(y_inner) 
            
            d1 = ttl.position()
            ttl.circle(inner_radius, 73)
            d2 = ttl.position()
            ttl.circle(inner_radius, 73)
            d3 = ttl.position()
            ttl.circle(inner_radius, 73)
            d4 = ttl.position()
            ttl.circle(inner_radius, 73)
            d5 = ttl.position()
            ttl.circle(inner_radius, 73)
            d6 = ttl.position()
            
            ttl.seth(0)
            
            
            #connect vertices to make star
            ttl.fillcolor("white")
            
            ttl.goto(c2)
            ttl.down()
            
            ttl.begin_fill()
            ttl.goto(d2)
            ttl.goto(c3)
            ttl.goto(d3)
            ttl.goto(c4)
            ttl.goto(d4)
            ttl.goto(c5)
            ttl.goto(d5)
            ttl.goto(c6)
            ttl.goto(d1)
            ttl.goto(c2)
            ttl.end_fill()
            
            ttl.up()
            ttl.goto(c1)
            ttl.seth(0)
            
            
            ttl.forward(2 * colWidth)
            
            

        new_y2 -= 2 * rowWidth
        y_inner = new_y2 +.7 * radius
        ttl.goto(new_x, new_y2)



def main():
    
    #Ask user for desired height of flag
    flagHeight = int(input("Enter height of flag in pixels: "))
    
    
    #Calculate dimensions of important shapes in flag
    flagWidth = flagHeight * 1.9
    
    
    #stripe measurements
    stripeHeight = flagHeight / 13
    
    stripeWidth = flagWidth
    
    
    #canton measurements
    cantonHeight = (7 / 13) * flagHeight
    
    cantonWidth = .4 * flagWidth 
    
    #starting coordinates for drawing
    startX = -(flagWidth / 2)
    startY = -(flagHeight / 2)
    
    #star measurements
    star_columnWidth = cantonWidth / 12
    
    star_rowWidth = cantonHeight / 10
    
    star_x = startX + star_columnWidth 
    
    star_y = startY + flagHeight - 1.5 * star_rowWidth
    
    star_radius = .4 * stripeHeight
    
    
    #screen measurements
    screenWidth = flagWidth + 200
    
    screenHeight = flagHeight + 200
    
    
    #Draw US flag
    import turtle
    
    ttl = turtle.Turtle()
    
    scr = turtle.Screen()
    
    scr.setup(screenWidth, screenHeight)

    drawStripes(startX, startY, stripeHeight, flagWidth, ttl)
    
    drawCanton(startX, startY, cantonHeight, cantonWidth, flagHeight, ttl)
    
    drawStars(star_x, star_y, star_radius, ttl, star_columnWidth, star_rowWidth)
    
    ttl.ht()
    
    ttl.done()
    #ttl.exitonclick()


    

main()