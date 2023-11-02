def solution():
    """Karen is considering her winter coat options. One coast costs $300 and will last for 15 years. The other coat costs $120 and will last for five years. How much money would Karen save over 30 years by buying the more expensive cost?"""
    # Calculate the total cost of the cheaper coat over 30 years
    cheaper_cost = 120 * 6  # $120 for 5 years and Karen needs to buy a new coat every 5 years for 30 years

    # Calculate the total cost of the more expensive coat over 30 years
    expensive_cost = 300 + (300/15) * 15 + (300/15) * 15 + (300/15) * (30-15)  # $300 for the first coat and $300/15 for the next 15 years

    # Calculate the savings of buying the more expensive coat
    savings = cheaper_cost - expensive_cost

    result = savings
    return result

print(solution())