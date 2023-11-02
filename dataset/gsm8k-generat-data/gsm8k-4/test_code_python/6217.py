def solution():
    """Levi has 5 lemons. Jayden has 6 more lemons than Levi. Jayden has one-third as many lemons as Eli has while Eli has one-half as many lemons as Ian has. How many lemons do they have in all?"""
    # Define the number of lemons Levi has
    levi_lemons = 5

    # Calculate the number of lemons Jayden has
    jayden_lemons = levi_lemons + 6

    # Calculate the number of lemons Eli has
    eli_lemons = jayden_lemons * 3

    # Calculate the number of lemons Ian has
    ian_lemons = eli_lemons * 2

    # Calculate the total number of lemons they have
    total_lemons = levi_lemons + jayden_lemons + eli_lemons + ian_lemons

    # return the result
    result = total_lemons
    return result

print(solution())