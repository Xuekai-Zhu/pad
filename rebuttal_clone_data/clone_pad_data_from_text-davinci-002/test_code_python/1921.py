def solution():
    number_of_candies = 36
    number_of_days = 7
    candies_eaten_per_day = 2
    days_eaten_candy = 2
    total_weeks = number_of_candies / (number_of_days * days_eaten_candy)
    result = total_weeks
    return result

print(solution())