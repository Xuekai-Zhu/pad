def solution():
    """Reggie, Lynn, and Paisley ran together. Paisley ran 4 miles. Reggie ran 5 times what Paisley ran and 3 miles farther than Lynn. How many miles did Lynn run?"""
    paisley_miles = 4
    reggie_miles = 5 * paisley_miles
    lynn_miles = reggie_miles - 3 - paisley_miles
    result = lynn_miles
    return result

print(solution())