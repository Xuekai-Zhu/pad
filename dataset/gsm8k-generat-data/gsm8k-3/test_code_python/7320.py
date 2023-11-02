def solution():
    """Alicia has 20 gumballs. Pedro has that many gumballs plus an additional number of gumballs equal to three times the number Alicia has. They put their gumballs in a bowl, and later Pedro takes out 40% of the gumballs to eat. How many gumballs are remaining in the bowl?"""
    # Define the number of gumballs Alicia has
    alicia_gumballs = 20

    # Calculate the number of gumballs Pedro has
    pedro_gumballs = alicia_gumballs + (alicia_gumballs * 3)

    # Calculate the total number of gumballs in the bowl
    total_gumballs = alicia_gumballs + pedro_gumballs

    # Calculate the number of gumballs Pedro takes out to eat
    pedro_eats = total_gumballs * 0.4

    # Calculate the number of gumballs remaining in the bowl
    remaining_gumballs = total_gumballs - pedro_eats

    # Display the number of gumballs remaining in the bowl
    result = remaining_gumballs
    return result

print(solution())