def solution():
    # Number of times animals were seen in January
    january_animals = 26

    # Number of times animals were seen in February
    february_animals = 3 * january_animals

    # Number of times animals were seen in March
    march_animals = february_animals / 2

    # Total number of times animals were seen in the first three months
    total_animals = january_animals + february_animals + march_animals
    result = total_animals
    return result

print(solution())