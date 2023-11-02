def solution():
    ahmed_age = 11  # Ahmed's current age
    fouad_age = 26  # Fouad's current age
    years = 0

    while fouad_age != ahmed_age * 2:
        fouad_age += 1
        ahmed_age += 1
        years += 1

    result = years
    return result

print(solution())