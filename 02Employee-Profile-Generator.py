# --- String Concatenation (Joining Strings) ---
first_name = 'John'
last_name = 'Doe'
# Using '+' to combine strings together with a space in between
full_name = first_name + ' ' + last_name

# --- Augmented Assignment (Appending to a String) ---
address = '123 Main Street'
# The '+=' operator appends a new string to the end of the existing variable
address += ', Apartment 4B'

# --- Type Conversion (Casting) ---
employee_age = 28
# Since employee_age is an integer, we must use str() to convert it to a string before concatenating
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
# Converting another integer to a string to safely print it alongside text
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# --- F-Strings (Formatted String Literals) ---
position = 'Data Analyst'
salary = 75000
# f'...' allows us to directly inject variables inside curly braces without manually converting types
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# --- String Slicing [start:stop] ---
employee_code = 'DEV-2026-JD-001'

# Takes characters from index 0 up to (but not including) index 3
department = employee_code[0:3]
print(department)

# Takes characters from index 4 up to index 8
year_code = employee_code[4:8]
print(year_code)

# Takes characters from index 9 up to index 11
initials = employee_code[9:11]
print(initials)

# --- Negative Slicing ---
# Using a negative index starts counting from the end of the string (-3 means the last 3 characters)
last_three = employee_code[-3:]
print(last_three)
