def solution():
    """Mark donates soup to the 6 homeless shelters.  Each one services 30 people and he decides to buy 10 cans of soup per person.  How many cans of soup does Mark donate?"""
    # Define the number of homeless shelters
    NUM_SHELTERS = 6

    # Define the number of people each shelter services
    PEOPLE_PER_SHELTER = 30

    # Define the number of cans of soup per person
    CANS_PER_PERSON = 10

    # Calculate the total number of cans of soup donated
    total_cans = NUM_SHELTERS * PEOPLE_PER_SHELTER * CANS_PER_PERSON

    # Display the total number of cans of soup donated
    result = total_cans
    return result

print(solution())