def solution():
    num_trucks = 3  # The farmer has 3 trucks to carry water
    num_tanks_per_truck = 3  # Each truck has 3 tanks
    tank_capacity = 150  # Each tank has a capacity of 150 liters

    # Calculate the total capacity of all tanks in all trucks
    total_capacity = num_trucks * num_tanks_per_truck * tank_capacity
    result = total_capacity
    return result

print(solution())