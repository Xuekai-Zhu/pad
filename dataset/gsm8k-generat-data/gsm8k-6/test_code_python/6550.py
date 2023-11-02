def solution():
    # Calculate the number of hybrid cars in the dealership
    hybrid_cars = 0.6 * 600

    # Calculate the number of hybrids with one headlight
    hybrids_one_headlight = 0.4 * hybrid_cars

    # Calculate the number of hybrids with full headlights
    hybrids_full_headlights = hybrid_cars - hybrids_one_headlight

    result = hybrids_full_headlights
    return result

print(solution())