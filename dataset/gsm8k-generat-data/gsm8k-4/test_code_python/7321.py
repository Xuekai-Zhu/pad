def solution():
    """A group of science students went on a field trip. They took 9 vans and 10 buses. There were 8 people in each van and 27 people on each bus. How many people went on the field trip?"""
    # Define the number of vans and the number of people in each van
    vans = 9
    van_capacity = 8

    # Define the number of buses and the number of people in each bus
    buses = 10
    bus_capacity = 27

    # Calculate the total number of people who went on the field trip
    total_people = (vans * van_capacity) + (buses * bus_capacity)

    # return the result
    result = total_people
    return result

print(solution())