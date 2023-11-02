def solution():
    """The region east of plain A is 50 square miles less than the region east of plain B. If plain B has 200 square miles, how many square miles do the plains have in total?"""
    region_a = region_b - 50
    region_b = 200
    total_region = region_a + region_b
    result = total_region
    return result

print(solution())