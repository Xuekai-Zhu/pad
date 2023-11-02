def solution():
    """Autumn was constantly misplacing her pencils. At the start of the school year, she purchased a pack of 20 pencils. In the first month of school, she misplaced 7 pencils, broke 3 pencils and had to throw them away, she found 4, and bought 2. How many pencils did Autumn have left?"""
    starting_pencils = 20
    misplaced_pencils = 7
    broken_pencils = 3
    found_pencils = 4
    bought_pencils = 2
    remaining_pencils = starting_pencils - misplaced_pencils - broken_pencils + found_pencils + bought_pencils
    result = remaining_pencils
    return result

print(solution())