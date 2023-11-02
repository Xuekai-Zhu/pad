def solution():
    """Marcus had 18 pebbles. He skipped half of them across the lake, but Freddy gave him another 30 pebbles. How many pebbles does Marcus have now?"""
    # Define the initial number of pebbles Marcus had
    initial_pebbles = 18

    # Calculate the number of pebbles Marcus skipped across the lake
    skipped_pebbles = initial_pebbles / 2

    # Calculate the total number of pebbles Marcus has now
    total_pebbles = skipped_pebbles + initial_pebbles + 30

    # Display the total number of pebbles Marcus has now
    result = total_pebbles
    return result

print(solution())