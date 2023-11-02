def solution():
    num_trucks = 3
    num_tanks_per_truck = 3
    tank_capacity = 150

    # Calculate the total number of tanks across all trucks
    total_tanks = num_trucks * num_tanks_per_truck

    # Calculate the total capacity of all tanks
    total_capacity = total_tanks * tank_capacity
    result = total_capacity
    return result

print(solution())