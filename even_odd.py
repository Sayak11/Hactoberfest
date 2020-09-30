

def even_odd(x):
    # Todo: Code to determine & print even or odd
    if (x % 2) == 0:
        print(x,"is Even".format(x))
    else:
        print(x,"is Odd".format(x))

print("Enter your number")
x=int(input().strip())
even_odd(x)
