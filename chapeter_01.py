#Chapter 1 - Fundamental data types


#1.1 
# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
new = ['Rowen','Sandeep']
baby_names.extend(new)

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Remove 'Aliza' from baby_names
baby_names.pop(1)

# Print baby_names
print(baby_names)

#1.2 Loop over records 
# Create the empty list: baby_names
baby_names = []

# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(records)
    
# Sort the names in alphabetical order
for name in sorted():
    # Print each name
    print(name)