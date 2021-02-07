#To show all digit occurances in a given number...

def digit_occurance():
    l=[0,0,0,0,0,0,0,0,0,0]
    try:
        n = int(input("Enter a number : "))
        if n<0:
            n=-n
        while(n>0):
            a=n%10
            l[a]+=1
            n//=10
        for i in range(len(l)):
            if(l[i]!=0):
                print(i," : ",l[i])
        
    except ValueError:
        print("Invalid input! integer expected...")

digit_occurance()



