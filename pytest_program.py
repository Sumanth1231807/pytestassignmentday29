def armstrong(x):
    sum = 0
    temp = x
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if x == sum:
        return True
    else:
        return False

def Divisible_or_not(x):
    if x%8==0:
        return True
    else:
        return False

def Smallest_of_threenum(x,y,z):
    if x<y and x<z:
        return x
    elif y<x and y<z:
        return y
    elif z<x and z<y:
        return z

def check_even_odd(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

def palindrome(my_str):
    reverse=(my_str[::-1])
    if my_str==reverse:
        return True
    else:
        return False

if __name__=="__main__":
    print("Armstrong or Not")
    x=int(input("Enter the Number "))
    armstrong=armstrong(x)
    print(armstrong)

    print("Divisible by 8 or not")
    x = int(input("Enter the Number "))
    divisible=Divisible_or_not(x)
    print(divisible)

    print("Smallest of three numbers")
    x=int(input("Enter num 1 "))
    y=int(input("Enter num 2 "))
    z=int(input("Enter num 3 "))
    smallest=Smallest_of_threenum(x,y,z)
    print(smallest)

    print("Enen or odd")
    x=int(input("Enter num 1 "))
    evenodd=check_even_odd(x)
    print(evenodd)

    print("palindrome or not")
    s=input("Enter the Word ")
    palindrome=palindrome(s)
    print(palindrome)



