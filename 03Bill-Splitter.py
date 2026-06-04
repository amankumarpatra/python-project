# --- Initializing the Tracker ---
# Starting with a running total of 0 dollars
running_total = 0

# The number of people sharing the bill
num_of_friends = 4

# --- Itemized Costs ---
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# --- Addition and Accumulation ---
# Using '+=' to add all the food items together and update the running total
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# --- Multiplication (Percentage Calculation) ---
# Multiplying by 0.25 to calculate a 25% tip amount
tip = running_total * 0.25
print('Tip amount:', tip)

# Adding the calculated tip to the running total
running_total += tip
print('Total with tip:', running_total)

# --- Division ---
# Dividing the grand total evenly among the number of friends
final_bill =  running_total / num_of_friends
print('Bill per person:', final_bill)

# --- Rounding Numbers ---
# round(value, 2) limits the long decimal result to exactly 2 decimal places for currency
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')
