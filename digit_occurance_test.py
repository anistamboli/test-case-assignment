
#code to check number of digit occurance in a number...

def test_occurance(n):
    l=[0,0,0,0,0,0,0,0,0,0]
    try:
        #n = int(input("Enter a number : "))
        if n<0:
            n=-n
        while(n>0):
            a=n%10
            l[a]+=1
            n//=10
        return(l)
    
    except ValueError:
        raise ValueError("Invalid input! integer expected...")

#digit_occurance(1281)



#Unit Testing code with cases...
import unittest

class TestDigitOccur(unittest.TestCase):
    def test_digit_occurance(self):
        #test for any not number value error 
        with self.assertRaises(ValueError):
            digit_occurance.test_occurance('xyz')

    def test_digit_occurance(self):
        #test for any positive no 1281
        result = test_occurance(1281)
        self.assertEqual(result,[0,2,1,0,0,0,0,0,1,0])

    def test_digit_occurance(self):
        #test for any positive no -900438
        result = test_occurance(-900438)
        self.assertEqual(result,[2,0,0,1,1,0,0,0,1,1])


if __name__ == '__main__':
    unittest.main()


