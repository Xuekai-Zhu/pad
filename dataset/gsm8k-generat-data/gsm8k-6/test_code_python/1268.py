def solution():
    # Calculate the total amount of toothpaste used per day by the family
    total_used_per_day = (3 + 2 + 1 + 1) * 3  # dad uses 3 grams, mom uses 2 grams, Anne and her brother use 1 gram each and they all brush 3 times a day

    # Calculate the number of days the toothpaste will last
    days = 105 / total_used_per_day
    result = days
    return result

print(solution())