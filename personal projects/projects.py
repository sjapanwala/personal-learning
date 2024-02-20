

# make a pyramid
def makePyramid(x):
    """
    builds a pyramid of what ever symbols are chosen, and how ever many layers the user desires
    """
    spaceVar = x - 2
    number = 1
    symbol = input("Please Enter a Symbol: ")
    while number != x+1:
        if number == 1:
            level = number * symbol
            space = (x - 1) * " "
            level = space + level
            number = number + 1
            print(level)
        else:
            leftSide = number - 1
            levelRight = number * symbol
            levelLeft = leftSide * symbol
            space = spaceVar * " "
            level =  space + levelLeft + levelRight
            number = number + 1
            print(level)    
            spaceVar = spaceVar - 1


def largestNumber(items):
    """
    Finds the largest number between a list of 4 numbers
    """ 
    itemLenght = len(items)
    itemHalf = itemLenght / 2
    itemHalf = int(itemHalf)
    firstHalf = items[0:itemHalf]
    lastHalf = items[itemHalf:]
    if len(firstHalf) and len(lastHalf) == 2:
        half1number1 = firstHalf[0]
        half1number2 = firstHalf[1]
        if half1number1 > half1number2:
            largestNumber1 = half1number1
        else:
            largestNumber1 = half1number2
        half2number1 = lastHalf[0]
        half2number2 = lastHalf[1]
        if half2number1 > half2number2:
            largestNumber2 = half2number1
        else:
            largestNumber2 = half2number2
        if largestNumber1 > largestNumber2:
            largestNumberList = largestNumber1
        else:
            largestNumberList = largestNumber2
    print(largestNumberList)






#usrInput = int(input("Please Enter Layer Numbers: "))
#makePyramid(usrInput)
myList = (123,17236,82137,109238)
largestNumber(myList)