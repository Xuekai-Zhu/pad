def solution():
    """Two buses leave a pick-up point station with 60% and 70% of capacity full, respectively. If the people in the buses are all employees of a company, and the buses have a capacity of 150, calculate the total number of the employees in the two buses combined?"""
    bus_capacity = 150
    bus_one = bus_capacity * 0.6
    bus_two = bus_capacity * 0.7
    total_employees = bus_one + bus_two
    result = total_employees
    return result

print(solution())