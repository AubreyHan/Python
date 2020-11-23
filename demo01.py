def collatz(number):
    print (number)
    if number%2 == 0:
        return int(number/2)
    else:
        return number*3+1


errNum = 1
while errNum == 1:
    try:
        i = int(input('Input your number:'))
        errNum = 0
    except ValueError:
        errNum = 1

while i != 1:
    i = collatz(i)
print (i)


        