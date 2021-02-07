# Random number generator between given range...

import time
def rand_val():
   try:
      x=int(input("Start Range: "))
      y=int(input("End Range: "))
      sub=y-x
      if sub<=0:
         return("End range must be greater than start...")
      else:
         random=int(time.time()*1000)
         random %=sub
         random+=x
         return(random)

   except ValueError:
      return("Invalid input!")

print(rand_val())
      
