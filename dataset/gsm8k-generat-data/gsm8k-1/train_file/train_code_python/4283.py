def solution():
    """Jeff had 300 pencils and donated 30% of them. Vicki had twice as many pencils as Jeff and donated 3/4 of his pencils. How many pencils are there remaining altogether?"""
    jeff_pencils = 300
    jeff_donated = jeff_pencils * 0.3
    jeff_remaining = jeff_pencils - jeff_donated
    
    vicki_pencils = jeff_pencils * 2
    vicki_donated = vicki_pencils * 0.75
    vicki_remaining = vicki_pencils - vicki_donated
    
    total_remaining = jeff_remaining + vicki_remaining
    result = total_remaining
    return result

print(solution())