def solution():
    """A farmer has three trucks to carry water to his farm. Each truck uses three tanks with a capacity of 150 liters of water. How many liters of water in total can the farmer carry in his trucks?"""
    num_trucks = 3
    tanks_per_truck = 3
    water_per_tank = 150
    total_water = num_trucks * tanks_per_truck * water_per_tank
    result = total_water
    return result

print(solution())