

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

# sorting algo for 4 numbers, can be increased with more if and else statements (for even numbers with factors of 2)
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

def findTheDifference():
    # there is a bug where it does not show the exact place where there is a discrepency
    """
    an algorithm to find the odd one out in a list
    - Press "stop" to stop the intake of the list
    """
    userList = []
    userInput = " "
    condition = True
    while userInput != "stop":
        userInput = input("Please Enter The Items: ")
        if userInput != "stop":
            userList.append(userInput)
    listLen = len(userList)
    counter = 0
    counter2 = 1
    while counter != listLen:
        if condition == True:
            if userList[counter] == userList[counter2]:
                counter = counter + 1
                counter2 = counter2 + 1
                condition =  True
            else:
                condition =  False
                print(userList)
                if counter == 0:
                    print("list is too short or list has greater than 1 abnoramlity or no abnormalities")
                else:
                    print(f"an abnormality detected at {counter}")
                counter = counter + 1
                counter2 = counter2 + 1
            
def sortObjects():
    """
    inputs a list of anything and sorts them into their categories
    - special characters/alphanumerics
    - numbers/integers
    - letters/strings
    """
    specialChars = []
    intChars = []
    strChars = []
    nonClassifyable = []
    
    # This list can be changed or altered to allow a user to input it
    userList = ["*", "!", "hello",5,10,500,2000,"this", "🔎", "😁😁❤🎶🌹"]  
    counter = 0
    while counter < len(userList):
        if isinstance(userList[counter], int):
            intChars.append(userList[counter])
        elif userList[counter].isalpha():
            strChars.append(userList[counter])
        elif not userList[counter].isalnum():
            specialChars.append(userList[counter])
        else:
            nonClassifyable.append(userList[counter])
        counter += 1
    
    print("Finished Sorting")
    print("Special Chars:", len(specialChars), "items")
    if len(specialChars) > 0:
        print(specialChars)
    print("Integer Chars:", len(intChars), "Items")
    if len(intChars) > 0:
        print(intChars)
    print("String Chars:", len(strChars), "Items")
    if len(strChars) > 0:
        print(strChars)
    print("Non-Classifyable:", len(nonClassifyable), "Items")
    if len(nonClassifyable) > 0:
        print(nonClassifyable)


def printPyramid():
    usrInput = int(input("Please Enter Layer Numbers: "))
    makePyramid(usrInput)
def printLargestNumber():
    myList = (123,17236,82137,109238)
    largestNumber(myList)
