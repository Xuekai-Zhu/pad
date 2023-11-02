def solution():
    tank_capacity = 100  # Tank can hold 100 liters of water
    initial_fill = tank_capacity * 2/5  # Tank is initially 2/5 filled with water
    water_collected_first_day = 15  # On the first day, 15 liters of water were collected
    water_collected_second_day = water_collected_first_day + 5  # On the second day, 5 more liters were collected than the first day
    water_needed_third_day = tank_capacity - (initial_fill + water_collected_first_day + water_collected_second_day)  # Water needed to fill the tank on the third day

    result = water_needed_third_day
    return result

print(solution())