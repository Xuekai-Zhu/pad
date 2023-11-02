def solution():
    tank_capacity = 18000  # The tank has a capacity of 18000 gallons
    water_filled_day1 = tank_capacity * (1/4)  # Wanda filled 1/4 of the tank's capacity with water on the first day
    water_pumped_day1 = water_filled_day1 * (3/4)  # Wanda pumped 3/4 as much water she pumped on the first day
    water_pumped_day2 = water_pumped_day1 * (2/3)  # Wanda pumped 2/3 of the amount of water she pumped on the second day
    water_pumped_day3 = water_pumped_day2 * (2/3)  # Ms. B pumped 2/3 of the amount of water she pumped on the second day
    water_pumped_day4 = water_pumped_day2 * (2/3)  # Ms. B pumped 2/3 of the amount of water she pumped

print(solution())