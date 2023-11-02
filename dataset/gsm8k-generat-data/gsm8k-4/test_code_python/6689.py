def solution():
    """Mark donates soup to the 6 homeless shelters. Each one services 30 people and he decides to buy 10 cans of soup per person. How many cans of soup does Mark donate?"""
    # Define the number of homeless shelters
    homeless_shelters = 6

    # Define the number of people served by each shelter
    people_served = 30

    # Define the number of cans of soup per person
    cans_per_person = 10

    # Calculate the total number of cans of soup donated
    total_cans = homeless_shelters * people_served * cans_per_person

    # Return the result
    result = total_cans
    return result

print(solution())