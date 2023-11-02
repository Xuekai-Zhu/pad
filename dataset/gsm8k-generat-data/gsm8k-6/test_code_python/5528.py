def solution():
    # Find the total number of cows the farmer has
    total_cows = 100  # Assume the farmer has 100 cows in total

    # Find the number of female cows the farmer has
    female_cows = total_cows - (0.4 * total_cows)

    # Find the total milk produced by female cows
    total_milk = female_cows * 2  # Each female cow produces 2 gallons of milk per day

    # Find the milk produced by 50 male cows
    male_milk = 50 * 0  # Assume male cows don't produce milk

    # Find the total milk produced per day by all cows
    total_milk += male_milk

    result = total_milk
    return result

print(solution())