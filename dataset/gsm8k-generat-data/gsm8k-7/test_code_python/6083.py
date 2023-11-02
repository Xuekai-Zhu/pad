def solution():
    die_rolls = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]

    # Calculate the current average of all rolls
    current_average = sum(die_rolls) / len(die_rolls)

    # Calculate the total sum needed for all rolls to have an average of 3
    target_sum = (len(die_rolls) + 1) * 3 - sum(die_rolls)

    # Calculate the minimum value needed on the next roll to reach the target sum
    next_roll_min = target_sum - 6

    result = next_roll_min
    return result

print(solution())