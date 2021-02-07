# test code to Check whether given number is perfect number or not...

def perfect_no(start,end):
    try:
        arr=[]
        for i in range(start,end+1):
            sum=0
            for j in range(1,(i//2)+1):
                if i%j==0:
                    sum+=j
            if sum==i:
                arr.append(i)
        return(arr)
    except ValueError:
        return("Invalid input! Range must be integer...")




#Test cases for number to perfect number check

import unittest   

class TestLetterCount(unittest.TestCase): 

    def test_letter_count(self):
        #test for range let 1-1000
        result = perfect_no(1,1000)
        self.assertEqual(result,[6, 28, 496])

        #test for range without perfect number
        result=perfect_no(100,200)
        self.assertEqual(result,[])


if __name__ == '__main__':
    unittest.main()
