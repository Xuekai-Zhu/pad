def solution():
    """Two buses leave a pick-up point station with 60% and 70% of capacity full, respectively. If the people in the buses are all employees of a company, and the buses have a capacity of 150, calculate the total number of the employees in the two buses combined?"""
    bus_capacity = 150
    first_bus_occupancy = 0.6
    second_bus_occupancy = 0.7
    first_bus_employees = first_bus_occupancy * bus_capacity
    second_bus_employees = second_bus_occupancy * bus_capacity
    total_employees = first_bus_employees + second_bus_employees
    result = total_employees
    return result

print(solution())