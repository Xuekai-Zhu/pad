def solution():
    # Calculate the amount of coffee the teacher drinks in a week
    coffee_per_day = (20 - 0.5*8) * 2  # 20-ounce thermos, 1/2 cup of milk, filled to the top, twice a day
    coffee_per_week = coffee_per_day * 5  # five-day school week
    reduced_coffee_per_week = coffee_per_week / 4  # reduced by 1/4
    result = reduced_coffee_per_week
    return result

print(solution())