def solution():
    """In a block of flats, there are 120 apartments. 85% of them have at least 1 resident, while 60% of the apartments have at least two residents. How many apartments have only one resident?"""
    # Define the number of apartments and the percentage with at least one resident
    total_apartments = 120
    at_least_one_percentage = 0.85

    # Calculate the number of apartments with at least one resident
    at_least_one = int(total_apartments * at_least_one_percentage)

    # Use the percentage with at least two residents to calculate the number of apartments with two or more residents
    at_least_two_percentage = 0.6
    at_least_two = int(total_apartments * at_least_two_percentage)

    # Calculate the number of apartments with only one resident
    only_one = at_least_one - (at_least_two - at_least_one)

    # Display the number of apartments with only one resident
    result = only_one
    return result

print(solution())