def solution():
    # Initialize the starting number of complaints
    complaints = 120

    # Increase complaints by 1/3rd when short-staffed
    complaints *= 1 + 1/3

    # Increase complaints by 20% when self-checkout is broken
    complaints *= 1 + 0.2

    # Multiply by number of days with the same conditions
    complaints *= 3

    result = complaints
    return result

print(solution())