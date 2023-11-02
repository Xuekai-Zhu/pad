def solution():
    """Bella has 10 earrings, which is 25% of Monica's earrings, and Monica has twice as many earrings as Rachel. How many earrings do all of the friends have?"""
    # Let's use variables for the number of earrings each person has
    # Let's set up an equation for each statement of the problem

    # "Bella has 10 earrings, which is 25% of Monica's earrings"
    b = 10
    b_as_percentage_of_m = 0.25
    m = b / b_as_percentage_of_m

    # "Monica has twice as many earrings as Rachel"
    m = 2 * r

    # Now we can substitute the second equation into the first
    # to get an equation just in terms of r
    b = 10
    b_as_percentage_of_m = 0.25
    m = 2 * r
    m_as_percentage_of_r = b_as_percentage_of_m * 4
    r = b / m_as_percentage_of_r

    # Now that we know r, we can use any of the equations to find b and m
    b = 10
    m = 2 * r

    # Finally, we can add up the number of earrings
    total_earrings = b + m + r

    result = total_earrings
    return result

print(solution())