def solution():
    # Define the number of trucks and tanks per truck
    num_trucks = 3
    tanks_per_truck = 3

    # Calculate the capacity of one tank
    tank_capacity = 150

    # Calculate the total water capacity of all tanks
    total_capacity = num_trucks * tanks_per_truck * tank_capacity

    result = total_capacity
    return result

print(solution())