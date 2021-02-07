
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
        
def mainfun(num):
    try:
        #num= int(input("Enter a number: "))    
        if(len(str(num))<=20):
            if num==0:
                res =("Shunya")
            elif (num>0):
                res = num_to_word(num)
            else :
                num=(-num)
                res =("Minus " + num_to_word(num))
        else:
            res=("Number is out of range")
        return(res)

    except ValueError:
        return("Invalid input. Number Expected...")



#Test cases for number to word problem

import unittest
class TestLetterCount(unittest.TestCase): 

    def test_letter_count(self):
        #test for zero/shunya
        result = mainfun(0)
        self.assertEqual(result,"Shunya")

    def test_num_to_word(self):
        #test for any positive number let 30287901239 
        result = mainfun(30287901239)
        self.assertEqual(result,'tri dasharab arab dva dashkoti asta koti sapta dashlaksh nava laksh dashahazar eka hazar dva shatam  nava trishant')


    def test_num_to_word(self):
        #test for any big number let 6734674648392847595736 
        result = mainfun(6734674648392847595736)
        self.assertEqual(result,'Number is out of range')

    def test_num_to_word(self):
        #test for any negative number let -87478460043
        result = mainfun(-87478460043)
        self.assertEqual(result,'Minus asta dasharab sapta arab catur dashkoti sapta koti asta dashlaksh catur laksh sat dashahazar  tri caturishant')



if __name__ == '__main__':
    unittest.main()
