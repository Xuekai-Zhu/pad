def solution():
    """Marcus is making calzones. It takes him 20 minutes to saute the onions and a quarter of that time to saute the garlic and peppers. It takes him 30 minutes to knead the dough, twice as long to let it rest, and 1/10th the combined kneading and resting time to assemble the calzones. How many minutes does Marcus spend on the calzones total?"""
    onion_saute_time = 20
    garlic_pepper_saute_time = onion_saute_time / 4
    dough_knead_time = 30
    dough_rest_time = 2 * dough_knead_time
    calzone_assemble_time = (dough_knead_time + dough_rest_time) / 10
    total_time = onion_saute_time + garlic_pepper_saute_time + dough_knead_time + dough_rest_time + calzone_assemble_time
    result = total_time
    return result

print(solution())