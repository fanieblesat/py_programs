value= 'not done'
largest = None
smallest = None
#User input
while value != 'done':
    value = input("Enter a number: ")
    if value == 'done':
       continue
    else:
        try:
            val=int(value)
        except:
            print("Invalid input")
        if smallest is None:
            smallest = val
        elif val < smallest:
            smallest = val
        if largest is None:
            largest = val
        elif val > largest:
            largest = val
#Printing values
print("The maximum number is:", largest)
print("The minimum number is:", smallest)
