def solution():
    # Define the number of salads needed
    salads_needed = 12

    # Calculate the number of lettuce plants needed, accounting for expected loss
    lettuce_plants_needed = (salads_needed * 2) / 3
    result = lettuce_plants_needed
    return result

print(solution())