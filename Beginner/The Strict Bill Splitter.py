# Take three inputs as strings: total bill amount (e.g., "1450.75"), 
# tip percentage (e.g., "12"), 
# and number of people (e.g., "4"). 
# Cast them to the appropriate numeric types, 
# calculate the exact per-person cost rounded to two decimal places using f-string formatting, 
# and print both the value and the type() of each variable at the end.

bill_amount = float(input('Enter total bill amount: '))
tip_percentage = float(input('Enter tip percentage: '))
num_people = int(input('Enter the number of people present: '))

tip_amount = bill_amount * (tip_percentage / 100)
total_bill_amount = bill_amount + tip_amount

cost_per_person = total_bill_amount / num_people

print(f'Per person cost is {cost_per_person:.2f} {type(cost_per_person)}')
print(f'Bill amount is {bill_amount} {type(bill_amount)}')
print(f'Tip in percentage is {tip_percentage} {type(tip_percentage)}')
print(f'Number of people are {num_people} {type(num_people)}')
print(f'Tip amount is  {tip_amount} {type(tip_amount)}')
print(f'Total bill amount is {total_bill_amount} {type(total_bill_amount)}')

