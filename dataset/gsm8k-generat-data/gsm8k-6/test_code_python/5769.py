def solution():
    # Calculate the total number of animals Zara has
    total_animals = 24 + 7 + x  # let x be the number of goats

    # Calculate the number of goats in each group
    goats_per_group = 48 - (24 + 7) // 3  # total number of goats divided into 3 groups with 24 cows and 7 sheep taken out

    # Calculate the total number of goats
    total_goats = goats_per_group * 3

    # Solve for x
    x = total_goats - (24 + 7)

    result = x
    return result

print(solution())