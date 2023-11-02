def solution():
    days_in_week = 7
    days_in_three_weeks = days_in_week * 3
    milk_containers_bought_per_day = 2
    total_milk_containers_bought = days_in_three_weeks * milk_containers_bought_per_day
    result = total_milk_containers_bought
    return result

print(solution())