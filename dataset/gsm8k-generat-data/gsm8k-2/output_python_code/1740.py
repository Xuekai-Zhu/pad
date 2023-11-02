def solution():
    """A farmer has three trucks to carry water to his farm. Each truck uses three tanks with a capacity of 150 liters of water. How many liters of water in total can the farmer carry in his trucks?"""
    tanks_per_truck = 3
    capacity_per_tank = 150
    total_trucks = 3
    total_capacity = tanks_per_truck * capacity_per_tank * total_trucks
    result = total_capacity
    return result

print(solution())