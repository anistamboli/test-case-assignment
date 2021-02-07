#check whether given input is palindrome or not....

def pal(strn):
    strn2= strn[::-1]
    if strn==strn2:
        print("Input is palindrome...")
    else:
        print("Not a palindrome")
    

string = input("Enter the input: ")
if len(string)!=0:
    pal(string)
else:
    print("Invalid input! Input string...")
