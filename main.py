

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
# ******************************
# Make your Code
# ******************************
prevNum = numbers[0]
counter = 0
for n in numbers:
    if insval > prevNum and insval < n:
        numbers.insert(numbers.index(n), insval)
        break
    elif insval < numbers[0]:
        numbers.insert(0, insval)
        break
    elif insval > n and counter == len(numbers) - 1: 
        numbers.insert(len(numbers), insval)
        break

    prevNum = n
    counter += 1
    
print(numbers)
