def solution():
    # Calculate the total number of households visited by Mark
    total_households = 20 * 5  # 20 households a day for 5 days

    # Calculate the number of households that gave Mark a pair of 20s
    giving_households = total_households / 2  # half of the households give Mark a pair of 20s

    # Calculate the total amount collected by Mark
    total_collected = giving_households * 40  # each pair of 20s is worth 40 dollars

    result = total_collected
    return result

print(solution())