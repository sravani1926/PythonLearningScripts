numbers=[5,2,1,7,4]

numbers.append(20)
print(numbers)
numbers.insert(0,10)
print(numbers)
numbers.remove(2)
print(numbers)
numbers.pop()
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.index(1))
numbers.clear()
print(numbers)
numbers=[2,2,4,6,7,4,1,3,5,9]
number2=numbers.copy()
print(number2)

#Q Write a program to remove duplicates
numbers=[2,2,4,6,7,4,1,3,5,9]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
