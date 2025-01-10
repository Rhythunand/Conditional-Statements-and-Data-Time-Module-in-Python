number = int(input("Enter number to check :"))

if number>50 :
  print("Number is greater than 50")
  if number % 2 == 0 :
    print("and it is even too")
  else :
    print("and it is odd")

else : 
  print("Number is less than 50")