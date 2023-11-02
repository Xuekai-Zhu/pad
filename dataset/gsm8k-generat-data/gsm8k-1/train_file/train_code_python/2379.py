def solution():
    """James has 3 gallons of milk. He drank 13 ounces of the milk. If there are 128 ounces in a gallon, how many ounces of milk does James have left?"""
    total_ounces = 3 * 128
    ounces_drunk = 13
    ounces_left = total_ounces - ounces_drunk
    result = ounces_left
    return result

print(solution())