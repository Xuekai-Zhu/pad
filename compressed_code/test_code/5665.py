def solution():
    
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