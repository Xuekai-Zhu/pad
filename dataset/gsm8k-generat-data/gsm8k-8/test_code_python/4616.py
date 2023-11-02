def solution():
    # Define the sacks of strawberries needed by each bakery per week
    bakery1 = 2
    bakery2 = 4
    bakery3 = 12

    # Calculate the total sacks needed by all the bakeries per week
    total_sacks_per_week = bakery1 + bakery2 + bakery3

    # Calculate the total sacks needed by all the bakeries in 4 weeks
    total_sacks_4_weeks = total_sacks_per_week * 4
    result = total_sacks_4_weeks
    return result

print(solution())