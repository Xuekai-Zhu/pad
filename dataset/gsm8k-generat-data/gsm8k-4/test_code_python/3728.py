def solution():
    """Marcus is making calzones. It takes him 20 minutes to saute the onions and a quarter of that time to saute the garlic and peppers. It takes him 30 minutes to knead the dough, twice as long to let it rest, and 1/10th the combined kneading and resting time to assemble the calzones. How many minutes does Marcus spend on the calzones total?"""
    # Calculate the time it takes to saute the onions
    onion_time = 20

    # Calculate the time it takes to saute the garlic and peppers
    gp_time = onion_time / 4

    # Calculate the time it takes to knead the dough, let it rest, and assemble the calzones
    dough_time = 30
    rest_time = dough_time * 2
    assembly_time = (dough_time + rest_time) / 10

    # Calculate the total time spent on the calzones
    total_time = onion_time + gp_time + dough_time + rest_time + assembly_time

    result = total_time
    return result

print(solution())