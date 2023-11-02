def solution():
    total_cows = 300  # There are 300 cows in the field
    female_cows = total_cows / 3 * 2  # There are twice as many females as males
    male_cows = total_cows - female_cows  # The rest are males

    # Calculate the number of females with spots
    females_spotted = female_cows / 2

    # Calculate the number of males with horns
    males_horned = male_cows / 2

    # Calculate the difference between the two
    difference = females_spotted - males_horned
    result = difference
    return result

print(solution())