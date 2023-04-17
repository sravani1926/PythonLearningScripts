#Type Conversion below will get error
#birth_year = input('Birth Year:')
#age = 2019 - birth_year
#print(age)


#Type Conversion below is correct
birth_year = int(input('Birth Year:'))
age = 2023 - birth_year
print(age)
print(type(age))

#Q: Ask a user theirweight(in pounds), convert it to kilograms and print on the terminal

weight_lbs= int(input('Weight(lbs):'))
weight_kg = weight_lbs * 0.45
print(weight_kg)

