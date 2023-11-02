def solution():
    """Tire repair for each tire costs $7, plus another 50 cents for sales tax. If Juan needs all 4 tires repaired, how much is the final cost?"""
    cost_per_tire = 7
    sales_tax = 0.5
    num_tires = 4
    total_cost = (cost_per_tire + sales_tax) * num_tires
    result = total_cost
    return result

print(solution())