def solution():
    """Ahmed is 11 years old and Fouad is 26 years old. In how many years will Fouad's age be double Ahmed's current age?"""
    # Define Ahmed and Fouad's ages
    ahmed_age = 11
    fouad_age = 26

    # Define the number of years to reach double Ahmed's current age
    years = 0

    # Iterate through the years until Fouad's age is double Ahmed's current age
    while fouad_age != ahmed_age * 2:
        fouad_age += 1
        ahmed_age += 1
        years += 1

    # return the result
    return years

print(solution())