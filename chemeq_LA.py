import re
from sympy import Matrix, lcm

elementList=[]
elementMatrix=[]
print("Please input your reactants.")
print("CASE SENSITIVE")
reactants=input("Reactants: ")
print("Please input your products.")
products=input("Products: ")
reactants=reactants.replace(' ', '').split("+")
products=products.replace(' ', '').split("+")

def addToMatrix(element, index, count, side):
    if(index == len(elementMatrix)):
        elementMatrix.append([])
        for x in elementList:
            elementMatrix[index].append(0)
    if(element not in elementList):
        elementList.append(element)
        for i in range(len(elementMatrix)):
            elementMatrix[i].append(0)
    column=elementList.index(element)
    elementMatrix[index][column]+=count*side
    if elementMatrix[index][column] == 0:
        elementList.remove(element)
        for row in elementMatrix:
            row.pop(column)


def findElements(segment,index, multiplier, side):
    elementsAndNumbers=re.split('([A-Z][a-z]?)',segment)
    i=0
    while(i<len(elementsAndNumbers)-1): # last element always blank
        i+=1
        if(len(elementsAndNumbers[i])>0):
            if(elementsAndNumbers[i+1].isdigit()):
                count=int(elementsAndNumbers[i+1])*multiplier
                addToMatrix(elementsAndNumbers[i], index, count, side)
                i+=1
            else:
                addToMatrix(elementsAndNumbers[i], index, multiplier, side)

def compoundDecipher(compound, index, side):
    segments=re.split('(\([A-Za-z0-9]*\)[0-9]*)',compound)
    for segment in segments:
        if segment.startswith("("):
            segment=re.split('\)([0-9]*)',segment)
            multiplier=int(segment[1])
            segment=segment[0][1:]
        else:
            multiplier=1
        findElements(segment, index, multiplier, side)

for i in range(len(reactants)):
    compoundDecipher(reactants[i],i,1)
for i in range(len(products)):
    compoundDecipher(products[i],i+len(reactants),-1)

elementMatrix = Matrix(elementMatrix)
elementMatrix = elementMatrix.transpose()

elementMatrix = elementMatrix.row_insert(elementMatrix.shape[0], Matrix([[0]*elementMatrix.shape[1]]))
elementMatrix = elementMatrix.col_insert(elementMatrix.shape[1], Matrix([0]*(elementMatrix.shape[0]-1)+[1]))

solution=elementMatrix.nullspace()[0]
multiple = lcm([val.q for val in solution])
solution = multiple*solution
coEffi=solution.tolist()
output=""

for i in range(len(reactants)):
    output+=str(coEffi[i][0])+reactants[i]
    if i<len(reactants)-1:
       output+=" + "
output+=" -> "
for i in range(len(products)):
   output+=str(coEffi[i+len(reactants)][0])+products[i]
   if i<len(products)-1:
       output+=" + "
       
print("THE BALANCED EQUATION IS: ")
print(output)
