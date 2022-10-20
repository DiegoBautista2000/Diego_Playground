#Income Tax Calculator 

tax_rate = 0.2
standard_deduction = 10000
gross_income = float(input("Enter the gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

if num_dependents >= 0:
    dependents_discount = num_dependents * 3000
    if gross_income > 0:
        adjusted_income = gross_income - (dependents_discount + standard_deduction)
        print("The income tax is", adjusted_income * tax_rate)
    else:
        print("Error - Your income can't be a negative number")
else:
    print("Error - Your numbers of dependents can't be a negative number") 

