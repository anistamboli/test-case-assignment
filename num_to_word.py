# Convert number to Sanskrit word generator

unit=["","eka ", "dva ", "tri ", "catur ","panca ", "sat ", "sapta ","asta ", "nava ", "dasa "]
tens=["","dasha","vishanti","trishant","caturishant","pancashant ", "shathi ", "saptati ","ashiti ", "navati "]
hundreds=["shatam","hazar","dashahazar","laksh","dashlaksh","koti","dashkoti","arab","dasharab","kharab","dashkharab","neel","dashneel","padma","dashpadma","shankh","dashshankh","mahashankh"]


def num_to_word(num):
    l=len(str(num))
    div=10**(l-1)
    res=""
    while(num//10>=10):
        pre=num//div
        num=num%div
        div=div//10
        res+= (unit[pre]+hundreds[l-3]+" ")
        l-=1
        if(num<100):
            res+=(" "+unit[num%10]+tens[num//10])
    return res
        
def main():
    try:
        num= int(input("Enter a number: "))    
        if(len(str(num))<=20):
            if num==0:
                res =("Shunya")
            elif (num>0):
                res = num_to_word(num)
            else :
                num=(-num)
                res =("Minus " + num_to_word(num))
        else:
            res="Number is out of range"
        print(res)

    except ValueError:
        print("Invalid input. Number Expected...")

main()



#test code for number to sanskrit word...

        
