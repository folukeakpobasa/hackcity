# fizzbuzz

number = int(input("Enter the number"))
list_number = []

for i in range(1, number+1):
    if i %  3 == 0 and i % 5 == 0 :
        list_number.append("FizzBuzz")
    elif i %  3 == 0 :
        list_number.append("Fizz")
    elif i % 5 == 0 :
        list_number.append("Buzz")
    else:
        list_number.append(str(i))
        
print(list_number)