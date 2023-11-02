def solution():
    """A 25 story building has 4 apartments on each floor. If each apartment houses two people, how many people does the building house?"""
    # Define the number of floors and apartments per floor
    num_floors = 25
    num_apartments_per_floor = 4

    # Calculate the total number of apartments in the building
    total_apartments = num_floors * num_apartments_per_floor

    # Calculate the total number of people in the building
    total_people = total_apartments * 2

    # return the result
    result = total_people
    return result

print(solution())