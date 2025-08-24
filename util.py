
xArray = []
yArray = []


def getxArray():
    return xArray

def getyArray():
    return yArray

def readFile():
    f = open("data\\Random5.tsp")

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