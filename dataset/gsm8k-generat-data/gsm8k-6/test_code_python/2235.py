def solution():
    # Calculate the total grams of fat from rice in a week
    fat_per_cup = 10  # grams of fat per cup of rice
    rice_in_a_day = 3 + 2 + 5  # total cups of rice consumed in a day
    fat_in_a_day = fat_per_cup * rice_in_a_day  # grams of fat consumed in a day
    fat_in_a_week = 7 * fat_in_a_day  # grams of fat consumed in a week
    result = fat_in_a_week
    return result

print(solution())