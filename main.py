ogString = input("Enter the Equation (Write ^x for any subscript):")


def inputHandling(firstEquation):
    sides = firstEquation.split('=')
    reactants = sides[0].split('+')
    reactantSplit = []
    
    products = sides[1].split('+')
    productSplit = []

    for i in range(len(reactants)):
        # Remove spaces first, then convert to list
        reactantSplit.append(list(reactants[i].replace(" ", "")))
    
    reactantDict = dict()

    for x in range(len(reactantSplit)):
        for y in range(len(reactantSplit[x])):
            if y > 0:
                if reactantSplit[x][y] == '^':
                    reactantDict.update({reactantSplit[x][y-1]:int(reactantSplit[x][y+1])})
                    
    for i in range(len(products)):
        # Remove spaces first, then convert to list
        productSplit.append(list(products[i].replace(" ", "")))
    
    productDict = dict()

    for x in range(len(productSplit)):
        for y in range(len(productSplit[x])):
            if y > 0 and y < len(productSplit[x]):
                if productSplit[x][y] == '^':
                    productDict.update({productSplit[x][y-1]:int(productSplit[x][y+1])})
    return reactantDict, productDict


print(inputHandling(ogString))
