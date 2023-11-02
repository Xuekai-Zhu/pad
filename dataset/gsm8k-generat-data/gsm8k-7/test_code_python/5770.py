def solution():
    eggs_per_dozen = 12
    eggs_to_store1 = 5 * eggs_per_dozen # supply 5 dozen eggs to store1
    eggs_to_store2 = 30 # supply 30 eggs to store2
    days_in_week = 7

    # Calculate the total number of eggs supplied to both stores in a day
    total_eggs_per_day = eggs_to_store1 + eggs_to_store2

    # Calculate the total number of eggs supplied to both stores in a week
    total_eggs_per_week = total_eggs_per_day * days_in_week
    result = total_eggs_per_week
    return result

print(solution())