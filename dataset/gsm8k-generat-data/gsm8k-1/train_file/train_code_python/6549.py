def solution():
    """In a car dealership with 600 cars, 60% of the cars are hybrids, and 40% of the hybrids contain only one headlight. How many of the hybrids have full headlights?"""
    total_cars = 600
    hybrid_cars = total_cars * 0.6
    hybrids_with_one_headlight = hybrid_cars * 0.4
    hybrids_with_full_headlights = hybrid_cars - hybrids_with_one_headlight
    result = hybrids_with_full_headlights
    return result

print(solution())