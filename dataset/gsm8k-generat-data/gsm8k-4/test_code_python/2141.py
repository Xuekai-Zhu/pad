def solution():
    """Jerry mows 8 acres of lawn each week. He mows ¾ of it with a riding mower that can cut 2 acres an hour. He mows the rest with a push mower that can cut 1 acre an hour. How long does Jerry mow each week?"""
    # Define the total area of the lawn and the area mowed with the riding mower
    total_area = 8 # acres
    riding_mower_area = 0.75 * total_area # acres

    # Calculate the time taken to mow with the riding mower
    riding_mower_time = riding_mower_area / 2 # hours

    # Calculate the area mowed with the push mower
    push_mower_area = total_area - riding_mower_area # acres

    # Calculate the time taken to mow with the push mower
    push_mower_time = push_mower_area / 1 # hours

    # Calculate the total time taken
    total_time = riding_mower_time + push_mower_time # hours

    result = total_time
    return result

print(solution())