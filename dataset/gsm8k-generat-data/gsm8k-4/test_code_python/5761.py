def solution():
    """A farmer has 52 cows. Each cow gives 5 liters of milk a day. How many liters of milk does the farmer get in a week?"""
    # Define the number of cows and the daily milk production per cow
    num_cows = 52
    milk_per_cow = 5

    # Calculate the total milk production for one day
    total_milk_per_day = num_cows * milk_per_cow

    # Calculate the total milk production for one week
    total_milk_per_week = total_milk_per_day * 7

    # Return the result
    result = total_milk_per_week
    return result

print(solution())