def solution():
    """A farmer has three trucks to carry water to his farm. Each truck uses three tanks with a capacity of 150 liters of water. How many liters of water in total can the farmer carry in his trucks?"""
    # Define the number of trucks and tanks per truck
    NUM_TRUCKS = 3
    TANKS_PER_TRUCK = 3

    # Define the capacity of each tank
    TANK_CAPACITY = 150

    # Calculate the total capacity of all tanks
    total_capacity = NUM_TRUCKS * TANKS_PER_TRUCK * TANK_CAPACITY

    # return the result
    result = total_capacity
    return result

print(solution())