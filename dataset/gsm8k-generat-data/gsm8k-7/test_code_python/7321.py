def solution():
    num_vans = 9
    num_buses = 10
    van_capacity = 8
    bus_capacity = 27

    # Calculate the total number of people in the vans
    total_van_people = num_vans * van_capacity

    # Calculate the total number of people in the buses
    total_bus_people = num_buses * bus_capacity

    # Calculate the total number of people on the field trip
    total_people = total_van_people + total_bus_people
    result = total_people
    return result

print(solution())