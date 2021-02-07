#Search any word occurance in given file if available...


def word_count(fname,search):
    with open(fname) as file:
        texts= file.read()
        words= texts.split()
    
    if(len(words)==0):
        print("Empty file")
    else :
        rec={}
        for word in words:
            if word in rec:
                rec[word]+=1
            else:
                rec[word]=1
        if search in rec:
            print(rec[search])
        else:
            print("Word not found...")
                

fname=input("Enter filename with extension in current directory: ")
search= input("Enter word to search: ")

word_count(fname,search)
