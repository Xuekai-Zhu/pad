def solution():
    """A group of science students went on a field trip. They took 9 vans and 10 buses. There were 8 people in each van and 27 people on each bus. How many people went on the field trip?"""
    num_vans = 9
    num_buses = 10
    van_capacity = 8
    bus_capacity = 27
    total_van_capacity = num_vans * van_capacity
    total_bus_capacity = num_buses * bus_capacity
    total_students = total_van_capacity + total_bus_capacity
    result = total_students
    return result

print(solution())