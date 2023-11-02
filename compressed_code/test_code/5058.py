def solution():
    
    total_cars = 600
    hybrid_cars = 0.6 * total_cars
    one_headlight_hybrids = 0.4 * hybrid_cars
    full_headlight_hybrids = hybrid_cars - one_headlight_hybrids
    result = full_headlight_hybrids
    return result

print(solution())