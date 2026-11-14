# Take three inputs as strings: total bill amount (e.g., "1450.75"), 
# tip percentage (e.g., "12"), 
# and number of people (e.g., "4"). 
# Cast them to the appropriate numeric types, 
# calculate the exact per-person cost rounded to two decimal places using f-string formatting, 
# and print both the value and the type() of each variable at the end.

bill_amt = float(input('Enter total bill amount:'))
tip = int(input('Enter tip percentage:'))
num_peopl = int(input('Enter the number of people present:'))


tips = bill_amt * (tip/100)
total_bill_amt = bill_amt + tips

val_person = total_bill_amt/ num_peopl

print(f'Per person cost is {val_person:.2f} {type(val_person)}')
