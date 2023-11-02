def solution():
    cows = 52  # The breeder owns 52 cows
    milk_per_cow_per_day = 1000  # Each cow produces 1000 oz of milk per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total amount of milk produced per week
    total_milk = cows * milk_per_cow_per_day * days_per_week
    result = total_milk
    return result

print(solution())