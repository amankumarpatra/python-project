# =====================================================================
# PROJECT: Ticket Booking Calculator
# PURPOSE: Demonstrates conditional logic, boolean operators, 
#          and arithmetic operations in Python.
# =====================================================================

# --- 1. CONFIGURATION & INITIALIZATION ---
# These variables simulate input data from a user or database
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# --- 2. ELIGIBILITY CHECKS ---
# Check if the user meets the minimum age requirement for any ticket
if age > 17:
    print('User is eligible to book a ticket')

# Check if the user is old enough to attend an Evening show
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# --- 3. DISCOUNT LOGIC ---
is_member = False
is_weekend = False
discount = 0

# A member must be 21 or older to qualify for this specific discount
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# --- 4. SURCHARGE LOGIC ---
extra_charges = 0
# Apply extra charges if it's the weekend OR if it's an evening show
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# --- 5. MAIN BOOKING VALIDATION & PRICING ---
# CRITICAL LOGIC: Evaluates booking permissions using operator precedence.
# Because 'and' takes precedence over 'or', it evaluates as:
# (age >= 21) or (age >= 18 and (show_time != 'Evening' or is_member))
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Determine service charges based on tier (Multi-way conditional)
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1  # Default fallback for Standard seats
    print('Service charges:', service_charges)

    # Calculate final total
    final_price = base_price + extra_charges + service_charges - discount
    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')
