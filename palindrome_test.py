#test code to check whether given input is palindrome or not....

def pal(strn):
    if len(strn)!=0:
        strn2= strn[::-1]
        if strn==strn2:
            return("Input is palindrome...")
        else:
            return("Not a palindrome")

    else:
        return("Invalid input! Input string...")
    
#print(pal(""))



# Test case checking for palindrome input or not...

import unittest

class TestLetterCount(unittest.TestCase):

    def test_letter_count(self):
        #test for not palindrome
        result = pal("ghfhfh")
        self.assertEqual(result,"Not a palindrome")

    def test_letter_count(self):
        #test for palindrome
        result = pal("kakak")
        self.assertEqual(result,"Input is palindrome...")

    def test_letter_count(self):
        #test for empty string
        result = pal("")
        self.assertEqual(result,"Invalid input! Input string...")
        
if __name__ == '__main__':
    unittest.main()






