def solution():
    """A 25 story building has 4 apartments on each floor. If each apartment houses two people, how many people does the building house?"""
    # Define the number of stories in the building
    stories = 25

    # Define the number of apartments on each floor
    apartments_per_floor = 4

    # Define the number of people in each apartment
    people_per_apartment = 2

    # Calculate the total number of apartments in the building
    total_apartments = stories * apartments_per_floor

    # Calculate the total number of people in the building
    total_people = total_apartments * people_per_apartment

    # Display the total number of people in the building
    result = total_people
    return result

print(solution())