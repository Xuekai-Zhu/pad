def solution():
    """Two buses leave a pick-up point station with 60% and 70% of capacity full, respectively. If the people in the buses are all employees of a company, and the buses have a capacity of 150, calculate the total number of the employees in the two buses combined?"""
    # Define the capacity of each bus
    BUS_CAPACITY = 150

    # Calculate the number of employees on the first bus
    bus1_occupancy = 0.6  # 60% occupancy
    bus1_employees = bus1_occupancy * BUS_CAPACITY

    # Calculate the number of employees on the second bus
    bus2_occupancy = 0.7  # 70% occupancy
    bus2_employees = bus2_occupancy * BUS_CAPACITY

    # Calculate the total number of employees on the two buses combined
    total_employees = bus1_employees + bus2_employees

    # Display the total number of employees
    result = total_employees
    return result

print(solution())