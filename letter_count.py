#to show maximum occured character (multiple characters if tied...)

def max_letter_count():
    dict={}
    str=input("Enter String : ")
    if(len(str)==0):
        print("Empty String")
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

        print("Maximum occured letter and its count: ")
        for key,value in dict.items():
            if(value==maxm):
                print(key," : ",value)


max_letter_count()
