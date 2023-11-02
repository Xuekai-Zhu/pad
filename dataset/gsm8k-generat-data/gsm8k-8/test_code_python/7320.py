def solution():
    # Define Alicia and Pedro's number of gumballs
    alicia_gumballs = 20
    pedro_gumballs = alicia_gumballs + 3 * alicia_gumballs

    # Calculate the total number of gumballs in the bowl
    total_gumballs = alicia_gumballs + pedro_gumballs

    # Calculate the number of gumballs remaining after Pedro eats 40%
    remaining_gumballs = total_gumballs - 0.4 * total_gumballs
    result = remaining_gumballs
    return result

print(solution())