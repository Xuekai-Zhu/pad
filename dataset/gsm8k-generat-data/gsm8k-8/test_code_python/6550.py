def solution():
    # Calculate the number of hybrids in the dealership
    hybrids = 600 * 0.6

    # Calculate the number of hybrids with only one headlight
    one_headlight = hybrids * 0.4

    # Calculate the number of hybrids with full headlights
    full_headlights = hybrids - one_headlight
    result = full_headlights
    return result

print(solution())