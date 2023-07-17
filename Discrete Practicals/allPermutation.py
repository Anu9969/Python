from itertools import permutations

def generate_permutations(digits):
    sorted_digits = sorted(digits)
    
    for perm in permutations(sorted_digits):
        yield ''.join(perm)

# Prompt the user to enter a set of digits
digit_str = input("Enter a set of digits (without spaces): ")
digits = list(digit_str)

# Generate permutations
permutations = list(generate_permutations(digits))

# Print the generated permutations
print("Permutations:")
for perm in permutations:
    print(perm)

