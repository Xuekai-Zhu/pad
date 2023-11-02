def solution():
    days_out_of_town = 14
    days_to_feed = days_out_of_town * 4
    food_per_day = 250
    total_food = days_to_feed * food_per_day
    result = total_food / 1000
    return result

print(solution())