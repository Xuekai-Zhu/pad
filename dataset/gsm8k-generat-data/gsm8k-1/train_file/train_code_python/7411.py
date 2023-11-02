def solution():
    """Marcus had 18 pebbles. He skipped half of them across the lake, but Freddy gave him another 30 pebbles. How many pebbles does Marcus have now?"""
    initial_pebbles = 18
    half_pebbles = initial_pebbles / 2
    additional_pebbles = 30
    total_pebbles = half_pebbles + initial_pebbles + additional_pebbles
    result = total_pebbles
    return result

print(solution())