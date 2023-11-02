def solution():
    """Tire repair for each tire costs $7, plus another 50 cents for sales tax. If Juan needs all 4 tires repaired, how much is the final cost?"""
    tire_cost = 7
    tax = 0.5
    num_tires = 4
    total_cost = (tire_cost + tax) * num_tires
    result = total_cost
    return result

print(solution())