def solution():
    """The total number of years in a century is the same as the number of marbles Gideon has. If he gives 3/4 of the marbles to his sister and multiples the number of remaining marbles by 2, he gets his age five years from now. How old is Gideon now?"""
    # Define the total number of marbles in a century
    MARBLES_IN_CENTURY = 100

    # Define the fraction of marbles Gideon gives to his sister
    FRACTION_GIVEN = 3/4

    # Calculate the number of marbles Gideon has left after giving some to his sister
    marbles_remaining = (1 - FRACTION_GIVEN) * MARBLES_IN_CENTURY

    # Calculate Gideon's age five years from now
    age_in_five_years = marbles_remaining * 2

    # Calculate Gideon's current age
    current_age = age_in_five_years - 5

    # Display Gideon's current age
    result = current_age
    return result

print(solution())