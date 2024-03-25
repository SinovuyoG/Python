num=5
a=5
def factorial(num):
    if type(num) is not int:
     return None
    if num < a :
      return None
    if num== 0:
        return None
    i=0
    f=1
    while i < num:
       i=i + 1
       f= f+1

 #Returns the value of the factorial of num if its defined, otherwise returns none
def factorial(num):
    if type(num) is not int:
        return None
    if num<a:
        return None
    if num==0:
        return 1

    return num* factorial(num-1)