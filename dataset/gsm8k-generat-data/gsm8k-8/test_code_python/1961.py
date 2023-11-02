def solution():
    candies_per_hour = 50
    total_candies = 4000
    hours_per_day = 10

    # Calculate the number of candies produced per day
    candies_per_day = candies_per_hour * hours_per_day

    # Calculate the number of days it will take to produce the required number of candies
    days_to_complete = total_candies // candies_per_day
    if total_candies % candies_per_day != 0:
        days_to_complete += 1

    result = days_to_complete
    return result

print(solution())