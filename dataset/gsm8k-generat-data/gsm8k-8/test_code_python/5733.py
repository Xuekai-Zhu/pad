def solution():
    # Calculate the number of marbles Gideon has
    num_years = 100
    num_marbles = num_years

    # Calculate the number of marbles Gideon has left after giving 3/4 to his sister
    remaining_marbles = num_marbles - (3/4 * num_marbles)

    # Calculate Gideon's age five years from now
    age_in_5_years = remaining_marbles * 2

    # Calculate Gideon's current age
    current_age = age_in_5_years - 5
    result = current_age
    return result

print(solution())