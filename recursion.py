#gift box eg having multiple gift boxes inside big one 
# A function that calls itself

# base case with recursion case
def open_gift_box(thing):
    if "ball" in thing: #---> base case
        return thing
    open_gift_box() #---> recursion case

#without base case it will loop infinitely which is called stack overflow
#Return statement is must for recursive function
def open_gift_box():
    open_gift_box()



#factorial eg: 4! = 4*3*2*1 = 24
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

op = factorial(5)
print(op)
