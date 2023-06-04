import matplotlib.pyplot as plt
import numpy as np
import random
import time

#Algorithm implementation
def bruteForceSolveVertAdjacencies(myList):
    # An empty list that will hold the rectangle information of the rectangles adjacent to the one being considered
    rectanglesadjs = []

    # We iterate through the list to consider each rectangle once
    for i, rect in enumerate(myList):
        adjs = []
        # A sublist is created to store the information of any rectangle that would be found to be adjacent to the rectangle on the ith position in the list 'rectangles'
        for j, adj_rect in enumerate(myList):
            # We iterate through the list to consider each rectangle in the list to try and compare it to the rectangle in the ith position 
            if i == j:
                continue

            if rect[2] == adj_rect[0]: # this is done to check if the right-hand side x value of the rectangle being considered in the outer loop is the same as the left-hand side x coordinate of the rectangle in the inner loop
                adjs.append(adj_rect) # if the above is evaluated to 'true', that rectangle is added on the adjacencies list in the ith position to indicate that it is adjacent to the rectangle in the ith position in the list 'rectangle'
        rectangle_info = f"{i+1}, {len(adjs)}" # concatenate rectangle number with adjacent rectangle count
        for adj_rect in adjs:
            rectangle_info += f", {adj_rect[0]}, {adj_rect[1]}, {adj_rect[2]}"
        rectanglesadjs.append(rectangle_info)
    return rectanglesadjs

#Everything below is used for generation of rectangles that will be used by the algorithm

#Define outer rectangle
xb = 1
yb = 1
xt = 20000
yt = 20000

x = np.array([xb,xt,xt,xb,xb])
y = np.array([yb,yb,yt,yt,yb])


rect = []

rect.append([xb,yb,xt,yt])




# Split the first 4 rectangles into 4 rectangles each
for k in range(5):
  
    new = rect.pop(0)

    xb = new[0]
    yb = new[1]
    xt = new[2]
    yt = new[3]

    if ((xt-xb) > 1000) and ((yt -yb) > 1000):
       

        midx = int((xt - xb)/2) + xb
        midy = int((yt - yb)/2) + yb
        rx = random.randint(midx-400,midx+400)
        ry = random.randint(midy-400,midy+400)

 

        rect.append([xb,yb,rx,ry])
        rect.append([xb,ry,rx,yt])
        rect.append([rx,yb,xt,ry])
        rect.append([rx,ry,xt,yt])


        for i in range(len(rect)):
            xb = rect[i][0]
            yb = rect[i][1]
            xt = rect[i][2]
            yt = rect[i][3]
        
            x1 = np.array([xb,xt,xt,xb,xb])
            y1 = np.array([yb,yb,yt,yt,yb])




# Choose a random rectange and split it into 4 rectangles
for i in range(2500):
    

    thisRect = random.randint(0,len(rect)-1)



    new = rect.pop(thisRect)


    xb = new[0]
    yb = new[1]
    xt = new[2]
    yt = new[3]

    if ((xt - xb) > 1000) and ((yt - yb) > 1000):
      

        midx = int((xt - xb)/2) + xb
        midy = int((yt - yb)/2) + yb
        rx = random.randint(midx-200,midx+200)
        ry = random.randint(midy-200,midy+200)

   

        rect.append([xb,yb,rx,ry])
        rect.append([xb,ry,rx,yt])
        rect.append([rx,yb,xt,ry])
        rect.append([rx,ry,xt,yt])
    else:
        rect.append(new)





#Main 

beginTime = time.time() #Starting timer
bruteForceSolveVertAdjacencies(rect)
endTime = time.time() #Stopping timer
time_taken_ms=(endTime - beginTime)*1000 #Time taken is converted to ms
print(len(rect),time_taken_ms) #This is used to print out the number of rectangles taken as input by the function written above as well as the time it took to run.
    
     



