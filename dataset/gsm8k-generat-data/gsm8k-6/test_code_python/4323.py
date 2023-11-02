def solution():
    # Calculate the total number of portions of formula Sandra has
    total_portions = 105
    # Calculate the number of portions needed per day
    portions_per_day = total_portions / 5
    # Calculate the number of portions per puppy per day
    portions_per_puppy = portions_per_day / 7
    result = portions_per_puppy
    return result

print(solution())