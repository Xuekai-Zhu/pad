def solution():
    # Define the amount of rice consumed per day
    rice_per_day = 3 + 2 + 5

    # Calculate the amount of rice consumed in a week
    rice_per_week = rice_per_day * 7

    # Calculate the amount of fat consumed in a week
    fat_per_week = rice_per_week * 10

    result = fat_per_week
    return result

print(solution())