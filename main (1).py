def Add (n1, n2):
  return n1 + n2

def Subtract (n1, n2):
  return n1 - n2

def Multiply (n1, n2):
  return n1 * n2

def Divide(n1,n2):
  return float(n1/n2)


def Calculator():
  print("1. Add \n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
  funC = int(input("Enter your choice: "))
  if funC > 5:
    print("Invalid choice")
    return
  
  num1=int(input("Choose first number:"))
  num2=int(input("Choose second number:"))
  if funC == 1:
    print(Add(num1, num2))

  elif funC == 2:
    print(Subtract(num1, num2))

  elif funC == 3:
    print(Multiply(num1, num2))

  elif funC == 4:
    print(Divide(num1, num2))
    
  elif funC == 5:
    print("Exit")
    return 

  else:
    print("Invalid Input")  


Calculator()