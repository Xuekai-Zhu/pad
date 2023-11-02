def solution():
    """Roman and Remy took separate showers. Remy used 1 more gallon than 3 times the number of gallons that Roman used for his shower. Together the boys used 33 gallons of water. How many gallons did Remy use?"""
    roman_gallons = (33 - 1) / 4
    remy_gallons = 3 * roman_gallons + 1
    result = remy_gallons
    return result

print(solution())