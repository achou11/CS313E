# File: Bowling.py
# Description: Program calculates game scores of a bowling game given file with the scores.
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E 
# Unique Number: 51320

# Date Created: 9/7/16
# Date Last Modified: 9/9/16


#function to identify number of pins hit based on symbol of throw
def value(ball, prev_ball = 0):
    
    #strikes = 10 pins
    if ball == "X":
        return 10

    #spares = 10 pins minus number of pins knocked down from the last throw
    if ball == "/":
        return 10 - prev_ball

    #gutter balls = 0 pins
    if ball == "-":
        return 0

    #return integer value of number if 1-9
    return int(ball)


#function to calculate game score and format output
def calcGameScore(throws):
    
    #variable to keep track of total score throughout game
    total = 0
    
    #line1 and line2 are used to format results for each frame
    line1 = "|"
    line2 = "|"
    
    #variable to keep track of which throw we're on in a list of throws
    ball = 0
    
    
    #Set conditions to calculate scores from frames 1-9 (10th frame will be done separately)
    frame = 1
    while frame <= 9:
        
        #ball1 and ball2 are strings of the balls in this specific frame
        ball1 = throws[ball]
        
        
        #check if first ball was a strike or not
        if ball1 != "X":
            
            #if not, assign next throw as ball2 of frame
            ball += 1
            ball2 = throws[ball]
            
            #check if they pick up spare or if frame is open
            if ball2 == "/":
                
                #frame_val is how much this frame is worth plus any bonuses
                #if ball2 is a spare, calculate bonus by adding the number of pins knocked down in next throw
                frame_value = 10 + value(throws[ball+1])
            
            #if frame is, frame_value is the sum of both throws in frame
            else:
                frame_value = value(ball1) + value(ball2)
        
            ball += 1
        
        else:
            
            #since frame is over if you get a strike, ball2 is just a space
            ball2 = " "
            
            #when a strike is thrown, calculate bonus by adding the value of the next 2 throws
            frame_value = 10 + value(throws[ball+1]) + value(throws[ball+2],value(throws[ball+1]))
            ball += 1
        
        #update line1 with the balls of this frame
        line1 += ball1 + " " + ball2 + "|"
        
        #add frame_val to the game total
        total += frame_value
        
        #update line2 with the current total; format string using rjust to keep correct format in double and triple digits
        line2 += str(total).rjust(3) + "|"
        
        frame += 1
      
      
    #rules for formatting and bonuses change in 10th frame
    if frame == 10:
        
        #3rd ball possible in 10th frame; create variable ball3 in case frame is open
        ball3 = " "
        
        #ball1 and ball2 defined right away since there are always at least 2 balls in 10th frame
        ball1 = throws[ball]
        ball += 1
        ball2 = throws[ball]
        
        if ball1 != "X":

            if ball2 == "/":
                #if there's a spare, save ball3 and calculate bonus (no extra bonus for another spare or strike)
                ball += 1
                ball3 = throws[ball]
                frame_value = 10 + value(ball3)
        
            else:
                #on an open 10th frame, ball3 remains blank
                frame_value = value(ball1) + value(ball2)

        else:
            #if there's a strike, save ball3 and calculate bonus (no extra bonus for any more strikes or spares)
            ball += 1
            ball3 = throws[ball]
            frame_value = 10 + value(ball2) + value(ball3,value(ball2))
            
        
        #Update first_line and second_line with results of 10th frame
        line1 += ball1 + " " + ball2 + " " + ball3 + "|"
        
        total += frame_value
        
        line2 += str(total).rjust(5) + "|"
    

    #print output in correct formatting

    print("  1   2   3   4   5   6   7   8   9   10")
    print("+---+---+---+---+---+---+---+---+---+-----+")
    print(line1)
    print(line2)
    print("+---+---+---+---+---+---+---+---+---+-----+")
    print()

    
def main():
    
    #create a list of all scores from scores.txt
    in_file = open("scores.txt", "r")
    
    score_list = []
    for line in in_file:
      score = line.strip()
      score = line.split()
      score_list.append(score)
  
    #calculate the total score for each game
    print()
    
    for game in score_list:
      calcGameScore(game)
                      
    print()             
          
        
            
        
              
    

            




main()