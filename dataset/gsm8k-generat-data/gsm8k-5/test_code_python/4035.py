def solution():
    pounds_per_pig_per_day = 10  # Randy feeds his pigs 10 pounds of feed per pig per day
    number_of_pigs = 2  # Randy has 2 pigs
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total amount of feed the pigs will be fed in one week
    total_feed = pounds_per_pig_per_day * number_of_pigs * days_per_week

    result = total_feed
    return result

print(solution())