def solution():
    # Calculate Bob's current savings
    current_savings = 100 * 2

    # Calculate the remaining amount needed for the puppy
    remaining_amount = 1000 - current_savings

    # Calculate the number of weeks Bob needs to win first place to reach his goal
    additional_weeks = remaining_amount // 100 + (remaining_amount % 100 != 0)

    result = additional_weeks
    return result

print(solution())