print("Please tell me two numbers: ") #comment 

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print("You entered: ", num1, "and", num2)
print("would you like to add or subtract these numbers? (Type 'add' or 'subtract')")
operation = input("Operation: ")    
if operation == "add": 
    final = num1 + num2
    print("The sum is: ", final)
elif operation == "subtract" :
    final = num1 - num2 
    print("The difference is: ", final)