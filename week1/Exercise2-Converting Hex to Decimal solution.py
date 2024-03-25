
hexNumbers={'0':0, '1':1, '2':2,'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
            'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

#Converts a string hexadecimal number into an integer decimal
#If hexNum is not valid hexadecimal number, return None

def hexInDec(hexnNum):
    hexNum=hexNumbers
    for char in hexNum:
        if char not in hexNumbers:
         return None
     
    if len(hexNum)==3:
         return hexNumbers(hexNum[0])* 256 + hexNumbers[hexNum[2]]
    hexInDec(5)