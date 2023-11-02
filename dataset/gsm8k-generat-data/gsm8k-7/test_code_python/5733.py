def solution():
    num_years_in_century = 100
    gideon_marbles = num_years_in_century

    # Calculate the number of marbles that Gideon gives to his sister
    marbles_given = 3/4 * gideon_marbles

    # Calculate the number of remaining marbles
    remaining_marbles = gideon_marbles - marbles_given

    # Calculate Gideon's age five years from now
    age_in_5_years = remaining_marbles * 2

    # Solve for Gideon's current age
    gideon_age = age_in_5_years - 5
    result = gideon_age
    return result

print(solution())