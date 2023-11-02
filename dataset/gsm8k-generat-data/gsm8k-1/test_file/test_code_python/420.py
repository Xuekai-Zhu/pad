def solution():
    """The employees of Google went on a day trip. 4 buses were rented that have the capacity of holding 60 employees. 6 minibusses that can hold 30 employees, and 10 minivans that can hold 15 employees. How many employees can join the day trip?"""
    bus_capacity = 60
    minibus_capacity = 30
    minivan_capacity = 15
    num_buses = 4
    num_minibuses = 6
    num_minivans = 10
    total_capacity = (bus_capacity * num_buses) + (minibus_capacity * num_minibuses) + (minivan_capacity * num_minivans)
    return total_capacity

print(solution())