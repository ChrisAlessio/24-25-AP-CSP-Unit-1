#   a114_divisible.py

# get two numbers from user
num1 = int(input("What is the first number"))
num2 = int(input("What is the second number"))
# loop while the numbers are not divisible (the remainder is not 0)
while num1 % num2 != 0:
  # inform user of result
  print("Number one is not equally divisible by Number two")
  # gather user input again
  num1 = int(input("What is the first number"))
  num2 = int(input("What is the second number"))
# inform user of result
print("Number one is equally divisible by number two")