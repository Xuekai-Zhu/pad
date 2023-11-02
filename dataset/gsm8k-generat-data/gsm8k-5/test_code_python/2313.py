def solution():
    # Set up equations using the given information
    # Let c = Christian's age now and b = Brian's age now
    # Christian is twice as old as Brian: c = 2b
    # In eight more years, Brian will be 40 years old: b + 8 = 40
    # Solve for Brian's age now: b = 32
    b = 32
    c = 2 * b
    christian_in_8_years = c + 8

    result = christian_in_8_years
    return result

print(solution())