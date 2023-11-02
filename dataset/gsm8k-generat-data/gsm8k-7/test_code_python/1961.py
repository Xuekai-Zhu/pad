def solution():
    candies_per_hour = 50
    total_candies = 4000
    hours_per_day = 10

    # Calculate the total hours needed to produce all candies
    total_hours = total_candies / candies_per_hour

    # Calculate the total days needed to complete the order
    total_days = total_hours / hours_per_day
    result = total_days
    return result

print(solution())