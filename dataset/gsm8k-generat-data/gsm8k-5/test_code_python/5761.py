def solution():
    cows = 52  # The farmer has 52 cows
    milk_per_cow_per_day = 5  # Each cow gives 5 liters of milk per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total milk in liters that the farmer gets in a week
    total_milk = cows * milk_per_cow_per_day * days_per_week
    result = total_milk
    return result

print(solution())