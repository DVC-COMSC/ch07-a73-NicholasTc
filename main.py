

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
# ******************************
# Make your Code
# ******************************
prevNum = numbers[0]
for n in numbers:
    if insval > prevNum and insval < n:
        numbers.insert(numbers.index(n), insval)
    elif insval < prevNum:
        numbers.insert(0, insval)
        break
    elif insval > n and insval > prevNum:
        numbers.insert(len(numbers), insval)
        break

    prevNum = n
    
print (numbers)
