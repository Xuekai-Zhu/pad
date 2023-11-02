def solution():
    """Marcus had 18 pebbles. He skipped half of them across the lake, but Freddy gave him another 30 pebbles. How many pebbles does Marcus have now?"""
    # Define the initial number of pebbles
    initial_pebbles = 18

    # Calculate the number of pebbles skipped across the lake
    skipped_pebbles = initial_pebbles / 2

    # Add the pebbles given by Freddy
    total_pebbles = skipped_pebbles + 30

    # Add the remaining pebbles
    total_pebbles += initial_pebbles - skipped_pebbles

    result = total_pebbles
    return result

print(solution())