def solution():
    bus_1_capacity = 150
    bus_1_fill_percentage = 0.6
    bus_2_capacity = 150
    bus_2_fill_percentage = 0.7

    # Calculate the number of employees in bus 1
    bus_1_employees = bus_1_capacity * bus_1_fill_percentage

    # Calculate the number of employees in bus 2
    bus_2_employees = bus_2_capacity * bus_2_fill_percentage

    # Calculate the total number of employees in both buses
    total_employees = bus_1_employees + bus_2_employees
    result = total_employees
    return result

print(solution())