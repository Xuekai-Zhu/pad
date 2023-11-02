def solution():
    cows = 52
    milk_per_cow_per_day = 5

    # Calculate total milk per day
    total_milk_per_day = cows * milk_per_cow_per_day

    # Calculate total milk per week
    total_milk_per_week = total_milk_per_day * 7

    result = total_milk_per_week
    return result

print(solution())