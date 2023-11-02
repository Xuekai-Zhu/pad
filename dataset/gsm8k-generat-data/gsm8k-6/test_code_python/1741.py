def solution():
    # Calculate the total capacity of water that the farmer's trucks can carry
    capacity_per_tank = 150  # liters of water per tank
    tanks_per_truck = 3  # number of tanks per truck
    trucks = 3  # number of trucks
    total_capacity = capacity_per_tank * tanks_per_truck * trucks
    result = total_capacity
    return result

print(solution())