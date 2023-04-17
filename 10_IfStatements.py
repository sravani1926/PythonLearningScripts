is_hot=True
if is_hot :
    print("It's a hot day")
    print("Drink Plenty of water")
else:
    print("It's a cold day")
    print("wear warm cloths")
print("Enjoy your Day")

is_hot=True
is_cold=True
if is_hot :
    print("It's a hot day")
    print("Drink Plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm cloths")
else:
    print("It's a lovely day")
print("Enjoy your Day")

#Q:price of a house is $1M If buyer has good credit they need to put downpayment 10% otherwise they need to put downpayment 20%
price=1000000
has_good_credit= True
if has_good_credit :
    down_payment = 0.1* price
else:
    down_payment=0.2*price
print(f"downpayment:$ {down_payment}")