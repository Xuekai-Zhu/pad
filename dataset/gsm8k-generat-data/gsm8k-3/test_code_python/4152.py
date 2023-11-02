def solution():
    """Karen is considering her winter coat options. One coast costs $300 and will last for 15 years. The other coat costs $120 and will last for five years. How much money would Karen save over 30 years by buying the more expensive cost?"""
    # Calculate the cost per year for each coat
    expensive_cost_per_year = 300 / 15
    cheap_cost_per_year = 120 / 5

    # Calculate the total cost over 30 years for each coat
    expensive_total_cost = expensive_cost_per_year * 30
    cheap_total_cost = cheap_cost_per_year * 30

    # Calculate the amount saved by buying the expensive coat
    amount_saved = cheap_total_cost - expensive_total_cost

    # Display the amount saved
    result = amount_saved
    return result

print(solution())