def solution():
    total_cars = 600  # Total number of cars in the dealership
    hybrids = round(total_cars * 0.6)  # Total number of hybrid cars
    one_headlight_hybrids = round(hybrids * 0.4)  # Number of hybrids with one headlight
    full_headlight_hybrids = hybrids - one_headlight_hybrids  # Number of hybrids with full headlights

    result = full_headlight_hybrids
    return result

print(solution())