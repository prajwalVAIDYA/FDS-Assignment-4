bal=0
n=int(input("Enter Number of transactions : "))
print("Transaction Format for Widrawal : W 200 and for Deposit : D 200 ")
for i in range (n):
  x=input("Enter transaction in format : ")
  tran=x.split(" ")
  op=tran[0]
  amt=int(tran[1])
  if op=="D":
    bal+=amt 
  elif op=="W":
    if (amt>bal):
      print("Insufficient Amount : ",amt)
    else:
      bal-=amt 
  else:
    print("Invalid Choice.")
print("\n")
print("Net A/c. Balance : ",bal)
