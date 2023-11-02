def solution():
    total_cars = 600
    hybrids = total_cars * (60 / 100)
    hybrids_with_one_headlight = hybrids * (40 / 100)
    hybrids_with_two_headlights = hybrids - hybrids_with_one_headlight
    result = hybrids_with_two_headlights
    return result

print(solution())