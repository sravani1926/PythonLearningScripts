#Example if applicant has high income and good credit then Eligible for loan
has_high_income = True
has_good_credit= True

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")
if has_high_income and not has_good_credit:
    print("Not Eligible for loan")

#Q: If name is less than 3 characters long print name must me atleast 3 characters otherwise if name is more than 50 characters print name must be maximum of 50 characters
#otherwise print name looks good

name= input("Enter name:")
if len(name)<3:
    print("name must me atleast 3 characters")
elif len(name)>50:
    print("name must be maximum of 50 characters")
else:
    print("Name Looks Good!!")
