def solution():
    """A group of science students went on a field trip. They took 9 vans and 10 buses. There were 8 people in each van and 27 people on each bus. How many people went on the field trip?"""
    num_vans = 9
    num_buses = 10
    people_per_van = 8
    people_per_bus = 27
    total_people = (num_vans * people_per_van) + (num_buses * people_per_bus)
    result = total_people
    return result

print(solution())