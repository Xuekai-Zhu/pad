def solution():
    # Define the capacity of the buses
    bus_capacity = 150

    # Calculate the number of employees in the first bus
    first_bus_occupancy = 0.6 * bus_capacity
    first_bus_employees = round(first_bus_occupancy)

    # Calculate the number of employees in the second bus
    second_bus_occupancy = 0.7 * bus_capacity
    second_bus_employees = round(second_bus_occupancy)

    # Calculate the total number of employees in the two buses
    total_employees = first_bus_employees + second_bus_employees
    result = total_employees
    return result

print(solution())