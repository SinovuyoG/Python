num1=int(input("Enter the first number"))
num2=int(input ("Enter the second number"))
def performOperation(operation):
    
    if operation == 'sum':
        return num1 + num2
    if operation =='multiply':
        return num1 * num2
    
print(performOperation('sum'))