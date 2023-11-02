def solution():
    # Calculate the cost of T-Mobile plan
    t_mobile_cost = 50 + 16 * 3  # $50 for first 2 lines and $16 for additional 3 lines

    # Calculate the cost of M-Mobile plan
    m_mobile_cost = 45 + 14 * 3  # $45 for first 2 lines and $14 for additional 3 lines

    # Calculate the difference in cost between the two plans
    difference = t_mobile_cost - m_mobile_cost
    result = difference
    return result

print(solution())