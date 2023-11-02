def solution():
    
    bus_capacity = 150
    first_bus_occupancy = 0.6
    second_bus_occupancy = 0.7
    first_bus_employees = first_bus_occupancy * bus_capacity
    second_bus_employees = second_bus_occupancy * bus_capacity
    total_employees = first_bus_employees + second_bus_employees
    result = total_employees
    return result

print(solution())