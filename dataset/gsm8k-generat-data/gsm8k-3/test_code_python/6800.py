def solution():
    """Autumn was constantly misplacing her pencils.  At the start of the school year, she purchased a pack of 20 pencils.  In the first month of school, she misplaced 7 pencils, broke 3 pencils and had to throw them away, she found 4, and bought 2.  How many pencils did Autumn have left?"""
    # Starting number of pencils
    pencils_start = 20

    # Pencils misplaced in the first month
    misplaced = 7

    # Pencils broken and thrown away
    broken = 3

    # Pencils found and bought
    found = 4
    bought = 2

    # Calculate the remaining number of pencils
    pencils_remaining = pencils_start - misplaced - broken + found + bought

    # Display the remaining number of pencils
    result = pencils_remaining
    return result

print(solution())