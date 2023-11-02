def solution():
    """A farmer has three trucks to carry water to his farm. Each truck uses three tanks with a capacity of 150 liters of water. How many liters of water in total can the farmer carry in his trucks?"""
    # Define the capacity of each tank
    TANK_CAPACITY = 150

    # Define the number of tanks per truck
    TANKS_PER_TRUCK = 3

    # Define the number of trucks
    NUM_TRUCKS = 3

    # Calculate the total capacity of all the tanks
    total_capacity = TANK_CAPACITY * TANKS_PER_TRUCK * NUM_TRUCKS

    # Display the total capacity
    result = total_capacity
    return result

print(solution())