def solution():
    # Calculate the amount of money Bob has saved up so far
    total_money = 200  # Bob won 100 dollars each for the first 2 weeks

    # Calculate the amount of money Bob needs to save to buy the puppy
    remaining_money = 1000 - total_money

    # Calculate the minimum number of additional weeks Bob needs to win first place
    additional_weeks = (remaining_money // 100) + (remaining_money % 100 > 0)  # round up to the nearest week
    result = additional_weeks
    return result

print(solution())