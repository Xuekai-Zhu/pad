def solution():
    # Define the number of lemons Levi has
    lemons_levi = 5

    # Calculate the number of lemons Jayden has
    lemons_jayden = lemons_levi + 6

    # Calculate the number of lemons Eli has
    lemons_eli = 2 * lemons_jayden

    # Calculate the number of lemons Ian has
    lemons_ian = 2 * lemons_eli

    # Calculate the total number of lemons
    total_lemons = lemons_levi + lemons_jayden + lemons_eli + lemons_ian
    result = total_lemons
    return result

print(solution())