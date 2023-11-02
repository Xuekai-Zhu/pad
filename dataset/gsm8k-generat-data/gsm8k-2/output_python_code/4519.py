def solution():
    """Cheryl has thrice as many colored pencils as Cyrus. Madeline has 63 colored pencils and only half of what Cheryl has. How many colored pencils do the three of them have altogether?"""
    madeline_pencils = 63
    cheryl_pencils = madeline_pencils * 2
    cyrus_pencils = cheryl_pencils / 3
    total_pencils = madeline_pencils + cheryl_pencils + cyrus_pencils
    result = total_pencils
    return result

print(solution())