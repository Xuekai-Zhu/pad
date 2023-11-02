def solution():
    
    # Define the number of cars and buses
    num_cars = 20
    num_buses = 12

    # Define the number of people carried by each bus
    num_people_per_bus = 35

    # Define the number of people carried by each bus
    num_people_per_bus = 3

    # Calculate the total number of people before the ceremony
    total_people_before = num_cars * num_people_per_bus

    # Calculate the total number of people after the ceremony
    total_people_after = num_buses * num_people_per_bus

    # Calculate the total number of people inside the church
    total_people = total_people_before + total_people_after

    # return the result
    result = total_people
    return result

print(solution())