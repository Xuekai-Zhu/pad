def solution():
    # Define the capacity of the spacecraft in terms of family units and people per family
    capacity_in_family_units = 300
    people_per_family = 4

    # Calculate the total capacity in terms of people
    total_capacity = capacity_in_family_units * people_per_family

    # Calculate the initial number of people on the ship
    initial_people = (1/3) * total_capacity - 100

    result = initial_people
    return result

print(solution())