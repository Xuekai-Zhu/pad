def solution():
    """There were sweets on the table. Jack came and took half of all the candies and 4 more candies. Then Paul came and took the remaining 7 sweets. How many sweets were on the table at first?"""
    paul_sweets = 7
    jack_sweets = (2 * paul_sweets) - 4
    total_sweets = paul_sweets + jack_sweets
    result = total_sweets
    return result

print(solution())