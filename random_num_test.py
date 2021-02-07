
#Test case code for random number generator...

def rand_val_test(x,y):
   try:
      sub=y-x
      if sub<=0:
         return("End range must be greater than start...")
      else:
         random=int(time.time()*1000)
         random %=sub
         random+=x
         return(random)

   except ValueError:
      print("Invalid input!")


#verification of random number using test cases

result=rand_val_test(1,10)
if result>=1 or result<=10:
   print('test for positive interval passed.')

result=rand_val_test(-100,-10)
if result>=-100 or result<=-10:
   print('test for negative interval passed.')

result=rand_val_test(100,10)
if result=="End range must be greater than start...":
   print('test for invalid input ranges passed.')
