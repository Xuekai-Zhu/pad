def solution():
    # Define the number of vans and the number of people in each van
    num_vans = 9
    people_per_van = 8

    # Define the number of buses and the number of people in each bus
    num_buses = 10
    people_per_bus = 27

    # Calculate the total number of people on the field trip
    total_people = (num_vans * people_per_van) + (num_buses * people_per_bus)
    result = total_people
    return result

print(solution())