def solution():
    """Ahmed is 11 years old and Fouad is 26 years old. In how many years will Fouad's age be double Ahmed's current age?"""
    ahmed_age = 11
    fouad_age = 26
    years = 0
    while fouad_age != ahmed_age * 2:
        fouad_age += 1
        ahmed_age += 1
        years += 1
    result = years
    return result

print(solution())