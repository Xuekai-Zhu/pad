def solution():
    """Karen is considering her winter coat options. One coat costs $300 and will last for 15 years. The other coat costs $120 and will last for five years. How much money would Karen save over 30 years by buying the more expensive coat?"""
    expensive_cost = 300
    expensive_years = 15
    cheap_cost = 120
    cheap_years = 5
    expensive_total_cost = expensive_cost 
    cheap_total_cost = cheap_cost 
    for i in range(2):
        expensive_total_cost += expensive_cost
        cheap_total_cost += cheap_cost
    expensive_cost_per_year = expensive_total_cost / expensive_years
    cheap_cost_per_year = cheap_total_cost / cheap_years
    expensive_total_cost_over_30_years = expensive_cost_per_year * 30
    cheap_total_cost_over_30_years = cheap_cost_per_year * 30
    
    savings = cheap_total_cost_over_30_years - expensive_total_cost_over_30_years
    result = savings
    
    return result

print(solution())