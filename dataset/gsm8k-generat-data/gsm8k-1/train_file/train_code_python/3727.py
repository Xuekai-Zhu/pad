def solution():
    """Marcus is making calzones. It takes him 20 minutes to saute the onions and a quarter of that time to saute the garlic and peppers. It takes him 30 minutes to knead the dough, twice as long to let it rest, and 1/10th the combined kneading and resting time to assemble the calzones. How many minutes does Marcus spend on the calzones total?"""
    onion_time = 20
    garlic_time = onion_time / 4
    pepper_time = onion_time / 4
    dough_time = 30
    rest_time = 2 * dough_time
    assemble_time = (dough_time + rest_time) / 10
    total_time = onion_time + garlic_time + pepper_time + dough_time + rest_time + assemble_time
    result = total_time
    return result

print(solution())