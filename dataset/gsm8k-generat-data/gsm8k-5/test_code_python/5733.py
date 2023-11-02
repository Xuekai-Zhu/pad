def solution():
    # Calculate the number of marbles Gideon has
    num_marbles = 100  # A century has 100 years

    # Calculate the number of marbles Gideon has after giving some to his sister
    num_marbles_remaining = (1/4) * num_marbles

    # Calculate Gideon's age five years from now
    age_in_five_years = (2 * num_marbles_remaining) + 5

    # Solve for Gideon's current age
    current_age = age_in_five_years - 5
    result = current_age
    return result

print(solution())