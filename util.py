
xArray = []
yArray = []


def getxArray():
    return xArray

def getyArray():
    return yArray

def readFile():

    # either this one or the other one will work, idk why it changes machine to machine

    #desktop works
    #f = open("data\\Random4.tsp")

    #laptop works
    f = open("data/Random12.tsp")

    stuf = f.readlines()

    str = stuf[7:]

    for z in range(len(str)):
        temp = str[z]

        space = temp.index(" ")

        temp = temp[space+1:]

        space = temp.index(" ")

        xValue = temp[:space]
        yValue = temp[space+1:]

        xValue = float(xValue)
        yValue = float(yValue)


        xArray.append(xValue)
        yArray.append(yValue)

        


#if __name__ == "__main__":
    #readFile()
    #print(xArray)
    #print(yArray)