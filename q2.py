def func():
    number = int(input("Enter the number : "))
    last_digit = number % 10
    if(last_digit % 3  == 0):
            print("divisible")
    else:
            print("sorry,not divisible")
    
func()