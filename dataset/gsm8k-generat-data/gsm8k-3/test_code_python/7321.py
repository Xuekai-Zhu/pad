def solution():
    """A group of science students went on a field trip. They took 9 vans and 10 buses. There were 8 people in each van and 27 people on each bus. How many people went on the field trip?"""
    # Define the number of vans, people per van, buses, and people per bus
    NUM_VANS = 9
    PEOPLE_PER_VAN = 8
    NUM_BUSES = 10
    PEOPLE_PER_BUS = 27

    # Calculate the total number of people on the field trip
    total_people = NUM_VANS * PEOPLE_PER_VAN + NUM_BUSES * PEOPLE_PER_BUS

    # Display the total number of people
    result = total_people
    return result

print(solution())