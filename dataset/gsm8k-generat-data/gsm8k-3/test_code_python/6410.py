def solution():
    """Moore's family compared mobile phone plans to get the best deal. At T-Mobile, the family plan costs $50 per month for the first two lines and $16 for each additional line. At M-Mobile, the family plan costs $45 for the first two lines and $14 for each additional line. Moore's family needs to purchase 5 cell phone lines. How much cheaper is the M-Mobile than T-Mobile?"""
    # Define the cost of the T-Mobile family plan
    T_MOBILE_FIRST_2 = 50
    T_MOBILE_ADDITIONAL = 16

    # Define the cost of the M-Mobile family plan
    M_MOBILE_FIRST_2 = 45
    M_MOBILE_ADDITIONAL = 14

    # Define the number of lines needed
    NUM_LINES = 5

    # Calculate the cost of the T-Mobile family plan
    if NUM_LINES <= 2:
        t_mobile_cost = T_MOBILE_FIRST_2
    else:
        t_mobile_cost = T_MOBILE_FIRST_2 + T_MOBILE_ADDITIONAL * (NUM_LINES - 2)

    # Calculate the cost of the M-Mobile family plan
    if NUM_LINES <= 2:
        m_mobile_cost = M_MOBILE_FIRST_2
    else:
        m_mobile_cost = M_MOBILE_FIRST_2 + M_MOBILE_ADDITIONAL * (NUM_LINES - 2)

    # Calculate the difference in cost between the two plans
    difference = t_mobile_cost - m_mobile_cost

    # Display the difference in cost
    result = difference
    return result

print(solution())