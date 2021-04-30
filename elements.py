


def calcElements(listOfNums):
    #print("len of : " + str(len(listOfNums)))
    lenOfList = len(listOfNums)
    sum = 0
    for i in range(0, len(listOfNums)):
        #print("i: " + str(i))
        sum = sum + listOfNums[i]
    #print("sum : " + str(sum))
    ave = sum / lenOfList
    #print("ave : " + str(ave))
    return ave


#calcElements([3, 4, 5])
