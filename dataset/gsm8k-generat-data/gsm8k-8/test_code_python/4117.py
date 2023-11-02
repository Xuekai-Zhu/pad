def solution():
    # Define Ahmed's and Fouad's current ages
    ahmed_age = 11
    fouad_age = 26

    # Define the number of years to add to Fouad's age
    years = 0

    # Continue adding years to Fouad's age until it is double Ahmed's age
    while fouad_age != 2 * ahmed_age:
        fouad_age += 1
        ahmed_age += 1
        years += 1

    result = years
    return result

print(solution())