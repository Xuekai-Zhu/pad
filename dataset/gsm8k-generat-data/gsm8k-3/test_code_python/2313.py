def solution():
    """Christian is twice as old as Brian. In eight more years, Brian will be 40 years old. How old will Christian be in eight years?"""
    # Let x be Brian's current age
    # Then Christian's current age is 2x
    x = 32 # solving for x: x + 8 = 40, x = 32
    christian_age = 2*x + 8
    result = christian_age
    return result

print(solution())