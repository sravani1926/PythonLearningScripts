#Weight Lbs->Kg/ Kg->Lbs

weight = int(input("Weight:"))
unit =input('(L)bs or (K)g')
if unit.upper()=='L':
    converted=weight*0.45
elif unit.upper()=='K':
    converted = weight / 0.45
else:
    print("wrong input")
print(f"Converted to({unit}): {converted}")