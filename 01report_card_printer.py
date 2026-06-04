# --- String Data Type ---
# 'Alice' is text, so Python assigns it the 'str' (string) type
name = 'Alice'
print(name, type(name))

# --- Boolean Data Type ---
# True/False values are used for conditional states and are type 'bool'
is_student = True
print(is_student, type(is_student))

# --- Integer Data Type ---
# Whole numbers without decimals are assigned the 'int' (integer) type
age = 20
print(age, type(age))

# --- Float Data Type & Type Checking ---
# Numbers with decimals are type 'float'
score = 80.5

# isinstance() checks if a variable matches a specific type, returning True or False
print(isinstance(score, float))

# Printing the value and confirming its type is <class 'float'>
print(score, type(score))
