# fibbonacci numbers
def fibo(n):
  num1=0
  num2=1
  next_number=num2
  count=2
  print(num1,"",num2,end="")
  while count<n:
    print(next_number,end="")
    count+=1
    num1,num2=num2,next_number
    next_number=num1=num2
n=int(input("enter the limit"))
fibo(n)
print()
