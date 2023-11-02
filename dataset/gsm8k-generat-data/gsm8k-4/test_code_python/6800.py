def solution():
    """Autumn was constantly misplacing her pencils. At the start of the school year, she purchased a pack of 20 pencils. In the first month of school, she misplaced 7 pencils, broke 3 pencils and had to throw them away, she found 4, and bought 2. How many pencils did Autumn have left?"""
    # Define the initial number of pencils
    initial_pencils = 20

    # Define the number of pencils misplaced, broken, found, and bought
    misplaced_pencils = 7
    broken_pencils = 3
    found_pencils = 4
    bought_pencils = 2

    # Calculate the total number of pencils remaining
    remaining_pencils = initial_pencils - misplaced_pencils - broken_pencils + found_pencils + bought_pencils

    result = remaining_pencils
    return result

print(solution())