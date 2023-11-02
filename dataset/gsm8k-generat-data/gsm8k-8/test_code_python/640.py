def solution():
    # Set initial variables
    total_ceilings = 28
    ceilings_painted_this_week = 12
    
    # Calculate how many ceilings will be painted next week
    ceilings_painted_next_week = 1/4 * ceilings_painted_this_week

    # Calculate how many ceilings will be left to paint after next week
    ceilings_left = total_ceilings - ceilings_painted_this_week - ceilings_painted_next_week

    result = ceilings_left
    return result

print(solution())