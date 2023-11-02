def solution():
    bus_capacity = 150  # The buses have a capacity of 150

    # Calculate the number of employees in the first bus
    num_employees_bus1 = bus_capacity * 0.6

    # Calculate the number of employees in the second bus
    num_employees_bus2 = bus_capacity * 0.7

    # Calculate the total number of employees in the two buses combined
    total_employees = num_employees_bus1 + num_employees_bus2
    result = total_employees
    return result

print(solution())