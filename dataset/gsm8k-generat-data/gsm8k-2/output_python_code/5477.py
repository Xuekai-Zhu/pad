def solution():
    """A tank can hold 100 liters of water. At the beginning of the rainy season, the tank is 2/5 filled with water. On the first day of the rainy season, the tank collected 15 liters of water. On the second day, 5 liters more water was collected than on the first day. On the third day, the tank was already filled. How many liters of water were collected on the third day?"""
    tank_capacity = 100
    initial_fill = tank_capacity * 2 / 5
    first_day_collect = 15
    second_day_collect = first_day_collect + 5
    total_collected = initial_fill + first_day_collect + second_day_collect
    third_day_collect = tank_capacity - total_collected
    result = third_day_collect
    return result

print(solution())