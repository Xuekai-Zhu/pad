def solution():
    """The age difference between Asaf and Alexander's age is half the total number of pencils Asaf has. The sum of their ages is 140, and Asaf is 50 years old. If Alexander has 60 more pencils than Asaf, calculate the total number of pencils they have together."""
    asaf_age = 50
    alex_pencils = asaf_pencils + 60
    age_diff = (asaf_pencils / 2)
    alex_age = 140 - asaf_age - age_diff
    total_pencils = asaf_pencils + alex_pencils
    result = total_pencils
    return result

print(solution())