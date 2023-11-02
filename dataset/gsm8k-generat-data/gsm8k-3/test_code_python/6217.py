def solution():
    """Levi has 5 lemons. Jayden has 6 more lemons than Levi. Jayden has one-third as many lemons as Eli has while Eli has one-half as many lemons as Ian has. How many lemons do they have in all?"""
    # Define the number of lemons Levi has
    lemons_levi = 5

    # Calculate the number of lemons Jayden has
    lemons_jayden = lemons_levi + 6

    # Calculate the number of lemons Eli has
    lemons_eli = lemons_jayden * 3

    # Calculate the number of lemons Ian has
    lemons_ian = lemons_eli * 2

    # Calculate the total number of lemons they have
    total_lemons = lemons_levi + lemons_jayden + lemons_eli + lemons_ian

    # Display the total number of lemons
    result = total_lemons
    return result

print(solution())