import math

xArray = [87.951292, 33.466597, 91.778314, 20.526749, 9.006012, 20.032350, 77.181310]
yArray = [2.658162, 66.682943, 53.807184, 47.633290, 81.185339, 2.761925, 31.922361]

positions = []


posToStartFrom = 0

#create each independent position variable with given data.  xArray.length == yArray.length MUST!
def setPositions():
    for x in range(len(xArray)):
        #create dictionary obj & add to position list
        pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False)
        positions.append(pos)

#method to find the closest position
def evalClosestPosition(posToStartFrom: int):

    lowestDistance = None
    pos = positions[posToStartFrom]

    #cycle thru all positions given the starting position
    for x in range(len(positions)):
        xValuep1 = pos['xValue']
        yValuep1 = pos['yValue']

        #if starting position is compared to itself == continue
        if positions[x] == positions[posToStartFrom]:
            continue
        else:
            #set second position to get ready for comparison
            pos2 = positions[x]
            xValuep2 = pos2['xValue']
            yValuep2 = pos2['yValue']

            #find distance between both pos's
            dist = math.sqrt((xValuep2 - xValuep1)**2 + (yValuep2 - yValuep1)**2)


            #set base lowest distance(edge case of only one other position)
            if lowestDistance == None:
                lowestDistance = dist
                tempd = dict(dPosition = pos2, distance = dist, spot = x)

            elif lowestDistance > dist:
                lowestDistance = dist
                tempd = dict(dPosition = pos2, distance = dist, spot = x)
            
            

            #print(xValuep1, " compared to ", xValuep2)
            #print(yValuep1, " compared to ", yValuep2, " with distance of ", dist)

    #pos2 = tempd['dPosition']
    #pos2['touched'] = True
    #tempd['dPosition'] = pos2
    #return a dictionary to have access to the distance and respective position
    return tempd



totalDistance = 0

def recursiveGumbo(PosStart: int):

    if len(positions) == 1:
        return 0


    var = evalClosestPosition(PosStart)

    print(PosStart, " to ", var['spot'])



    spot = var['spot']
    print(var['distance'])

    if positions[spot] == positions[len(positions)-1]:
        positions.pop(spot)
        return recursiveGumbo(0)+var['distance']
            
    else:
        positions.pop(spot)
        return recursiveGumbo(spot)+var['distance']
            
    




    

    











if __name__ == "__main__":
    setPositions()

    print(positions)


    firstPosition = evalClosestPosition(posToStartFrom)
    firstPosition['touched'] = True
    totalDistance+=firstPosition['distance']

    print(posToStartFrom, " to ", firstPosition['spot'])

    totalDistance+=recursiveGumbo(firstPosition['spot'])

    print("Shortest Distance Brute Force : ", totalDistance)

    #print(evalClosestPosition(posToStartFrom))