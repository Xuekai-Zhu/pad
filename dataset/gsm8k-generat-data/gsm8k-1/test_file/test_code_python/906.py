def solution():
    """Farmer Brown's farm is 200 acres, and Farmer Smith's farm is 100 acres more than twice that. How many acres do the two farms have, together?"""
    brown_farm = 200
    smith_farm = 2 * brown_farm + 100
    total_acres = brown_farm + smith_farm
    result = total_acres
    return result

print(solution())