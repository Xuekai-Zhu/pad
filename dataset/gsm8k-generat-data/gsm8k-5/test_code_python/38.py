def solution():
    # Determine the amount of tea for one cup
    tea_per_cup = 1 / 8 # 1 ounce of tea in an 8 ounce cup

    # Determine the amount of tea for all cups at the party
    cups_at_party = 12
    tea_for_party = cups_at_party * (6 / 8) # 6 ounce cup divided by 8 to get tea per cup

    # Determine the total amount of tea needed for the party
    total_tea = tea_for_party / tea_per_cup

    result = total_tea
    return result

print(solution())