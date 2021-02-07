#code to Search any word occurance in given file if available...

def word_count(fname,search):
    with open(fname) as file:
        texts= file.read()
        words= texts.split()
    
    if(len(words)==0):
        return("Empty file")
    else :
        rec={}
        for word in words:
            if word in rec:
                rec[word]+=1
            else:
                rec[word]=1
        if search in rec:
            return(rec[search])
        else:
            return("Word not found...")
                




#Test cases to check any words occurance in a given file...

import unittest   

class TestLetterCount(unittest.TestCase): 

    def test_letter_count(self):
        #test for word available most in file
        result = word_count('a.txt','wa')
        self.assertEqual(result,7)

        #test for any single word
        result=word_count('a.txt','yappari')
        self.assertEqual(result,1)

        #test for no word
        result=word_count('a.txt','gilgamesh')
        self.assertEqual(result,"Word not found...")


if __name__ == '__main__':
    unittest.main()
