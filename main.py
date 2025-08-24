import math

import util

#xArray = [87.951292, 33.466597, 91.778314, 20.526749, 9.006012, 20.032350, 77.181310]
#yArray = [2.658162, 66.682943, 53.807184, 47.633290, 81.185339, 2.761925, 31.922361]

xArray = []
yArray = []

positions = []


posToStartFrom = 0

#create each independent position variable with given data.  xArray.length == yArray.length MUST!
def setPositions():
    util.readFile()

    xArray = util.getxArray()
    yArray = util.getyArray()


    for x in range(len(xArray)):
        #create dictionary obj & add to position list
        pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False)
        positions.append(pos)

    print(xArray)
    print(yArray)

#method to find the closest position
def evalClosestPosition(posToStartFrom: int):

    lowestDistance = None
    traveledPos = None
    spot = None

    pos = positions[posToStartFrom]

    #cycle thru all positions given the starting position
    for x in range(len(positions)):
        xValuep1 = pos['xValue']
        yValuep1 = pos['yValue']

        #if starting position is compared to itself == continue
        if positions[x] == positions[posToStartFrom]:
            continue
        else:
            #iterate thru positions we havnt visited
            if positions[x]['touched'] == False:
                #set second position to get ready for comparison
                pos2 = positions[x]
                xValuep2 = pos2['xValue']
                yValuep2 = pos2['yValue']

                #find distance between both pos's
                dist = math.sqrt((xValuep2 - xValuep1)**2 + (yValuep2 - yValuep1)**2)


                #set base lowest distance(edge case of only one other position)
                #also we update any needed values if we end up going with this position as our closest
                #i.e our position value, lowest distance, and our position in the positions list
                if lowestDistance == None:
                    lowestDistance = dist
                    traveledPos = pos2
                    spot = x

                elif lowestDistance > dist:
                    lowestDistance = dist
                    traveledPos = pos2
                    spot = x
            

            #print(xValuep1, " compared to ", xValuep2)
            #print(yValuep1, " compared to ", yValuep2, " with distance of ", dist)

    #pos2 = tempd['dPosition']
    #pos2['touched'] = True
    #tempd['dPosition'] = pos2
    #return a dictionary to have access to the distance and respective position


    #We set the touched value to true once we have visited that position
    traveledPos['touched']=True
    tempd = dict(dPosition = traveledPos, distance = lowestDistance, spot = spot)
    return tempd



totalDistance = 0

def recursiveGumbo(PosStart: int):

    #boolean value to check if there is any values that have not been touched
    anyLeft = False

    #a count value to be used when:  there is only one value left to open up the first position to create a hamiltonian
    count = 0

    for x in range(len(positions)):
        if positions[x]['touched'] == False:
                count+=1
                #we found that there are some left, sooo we dont end the recursion
                anyLeft = True


    if anyLeft == False:
        #none left so we end it
        print("None left")
        return 0
    
    #if theres one value left that still needs to be 'touched' we go ahead and add our start pos so we can create that loop
    elif count == 1:
        #adding out original starting point back into the mix
        positions[posToStartFrom]['touched'] = False

    #finds position that is closest to ours, that also hasnt been 'touched' yet
    var = evalClosestPosition(PosStart)

    print(PosStart, " to ", var['spot'])



    spot = var['spot']
    print(var['distance'])

    return recursiveGumbo(spot)+var['distance']
            
    




    

    











if __name__ == "__main__":
    setPositions()

    #print(positions)

    #Goes ahead and sets up the first position
    positions[posToStartFrom]['touched'] = True
    firstPosition = evalClosestPosition(posToStartFrom)
    totalDistance+=firstPosition['distance']

    #Display where we going to
    print(posToStartFrom, " to ", firstPosition['spot'])

    #add up total distance recursively
    totalDistance+=recursiveGumbo(firstPosition['spot'])


    print("Shortest Distance Brute Force : ", totalDistance)