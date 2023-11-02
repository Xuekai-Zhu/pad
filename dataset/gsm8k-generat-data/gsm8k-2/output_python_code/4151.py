def solution():
    """Karen is considering her winter coat options. One coast costs $300 and will last for 15 years. The other coat costs $120 and will last for five years. How much money would Karen save over 30 years by buying the more expensive cost?"""
    expensive_cost = 300
    expensive_lifetime = 15
    cheap_cost = 120
    cheap_lifetime = 5
    expensive_cost_per_year = expensive_cost / expensive_lifetime
    cheap_cost_per_year = cheap_cost / cheap_lifetime
    savings_per_year = cheap_cost_per_year - expensive_cost_per_year
    total_savings = 30 * savings_per_year
    result = total_savings
    return result

print(solution())