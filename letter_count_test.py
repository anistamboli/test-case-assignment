#test code to show maximum occured character (multiple characters if tied...)
                
def max_letter_test(str):
    dict={}
    #str=input("Enter String : ")
    if(len(str)==0):
        return ("Empty String")
    else :
        for i in str:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
                
        maxm=0
        for count in dict.values():
            if count>maxm:
                maxm=count
        return (dict)

        print("Maximum occured letter and its count: ")
        for key,value in dict.items():
            if(value==maxm):
                print(key," : ",value)

#max_letter_test('jhbdsbjhd')



# Test code for maximum letter count...

import unittest

class TestLetterCount(unittest.TestCase):
    def test_letter_count(self):
        #test for any string
        result = max_letter_test(1281)
        self.assertEqual(result,{'j': 2, 'h': 2, 'b': 2, 'd': 2, 's': 1})

    def test_letter_count(self):
        #test for empty string
        result = max_letter_test("")
        self.assertEqual(result,"Empty String")


if __name__ == '__main__':
    unittest.main()






