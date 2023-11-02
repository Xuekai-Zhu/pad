def solution():
    """The total number of years in a century is the same as the number of marbles Gideon has. If he gives 3/4 of the marbles to his sister and multiples the number of remaining marbles by 2, he gets his age five years from now. How old is Gideon now?"""
    # Define the total number of marbles in a century
    century_years = 100
    total_marbles = century_years

    # Calculate the number of marbles Gideon has after giving 3/4 to his sister
    remaining_marbles = total_marbles * 0.25

    # Calculate Gideon's age in 5 years
    age_in_5_years = remaining_marbles * 2

    # Calculate Gideon's current age
    current_age = age_in_5_years - 5

    result = current_age
    return result

print(solution())