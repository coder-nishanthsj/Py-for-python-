
#python program to find factorial of given number and sum of natural numbers
def fact(n):
   return 1 if (n==1 or n==0)else n*fact(n-1);
def sum(n):
   return 0 if (n==0)else (n-1);
num=int(input("enter any number:"))
print("1-to find the factorial,2-to find the sum 3-exit")
opt=int(input("enter the option 1-3:"))
if(opt==1):
   print("factorial of ",num,"is:",fact(num))
else:
    if(opt==2):
     print("sum of",num,"is:",sum(num))
     else:
         print("")
           
