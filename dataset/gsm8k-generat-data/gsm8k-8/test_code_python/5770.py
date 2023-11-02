def solution():
    # Define the number of eggs supplied to the first store per day
    eggs_per_day_store1 = 5 * 12

    # Define the number of eggs supplied to the second store per day
    eggs_per_day_store2 = 30

    # Calculate the total number of eggs supplied to both stores per day
    total_eggs_per_day = eggs_per_day_store1 + eggs_per_day_store2

    # Calculate the total number of eggs supplied to both stores in a week
    total_eggs_per_week = total_eggs_per_day * 7
    result = total_eggs_per_week
    return result

print(solution())