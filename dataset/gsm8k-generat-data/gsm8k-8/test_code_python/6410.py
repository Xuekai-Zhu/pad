def solution():
    # Calculate cost for T-Mobile
    t_mobile_cost = 50 + 16 * 3  # First two lines and additional three lines

    # Calculate cost for M-Mobile
    m_mobile_cost = 45 + 14 * 3  # First two lines and additional three lines

    # Calculate price difference
    price_difference = t_mobile_cost - m_mobile_cost
    result = price_difference
    return result

print(solution())