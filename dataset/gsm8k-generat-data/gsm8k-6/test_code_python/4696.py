def solution():
    # Calculate the number of people in each bus
    bus1_capacity = 150 * 0.6
    bus2_capacity = 150 * 0.7

    # Calculate the total number of employees in both buses
    total_employees = int(bus1_capacity + bus2_capacity)
    result = total_employees
    return result

print(solution())