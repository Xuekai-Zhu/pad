def solution():
    """Mr. Reyansh has a dairy farm with 40 cows. Each cow on the farm drinks 80 liters of water daily. He also has a sheep ranch with 10 times the number of cows, with each sheep drinking 1/4 times as much water as a cow does. How many liters of water does Mr. Reyansh use to water all of his animals in a week?"""
    cow_count = 40
    cow_water_per_day = 80
    cow_water_per_week = cow_count * cow_water_per_day * 7

    sheep_count = cow_count * 10
    sheep_water_per_day = cow_water_per_day * 0.25
    sheep_water_per_week = sheep_count * sheep_water_per_day * 7

    total_water_per_week = cow_water_per_week + sheep_water_per_week
    result = total_water_per_week
    return result

print(solution())