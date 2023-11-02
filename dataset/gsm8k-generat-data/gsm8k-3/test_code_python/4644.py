def solution():
    """Roman and Remy took separate showers. Remy used 1 more gallon than 3 times the number of gallons that Roman used for his shower. Together the boys used 33 gallons of water.  How many gallons did Remy use?"""
    # Let x be the number of gallons Roman used
    # Remy used 1 more gallon than 3 times Roman's usage
    # Remy used 3x + 1 gallons
    # Together the boys used 33 gallons
    # x + (3x+1) = 33
    # 4x = 32
    # x = 8
    roman_usage = 8
    remy_usage = 3 * roman_usage + 1
    result = remy_usage
    return result

print(solution())