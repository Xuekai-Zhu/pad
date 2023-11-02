def solution():
    """James has 3 gallons of milk. He drank 13 ounces of the milk. If there are 128 ounces in a gallon, how many ounces of milk does James have left?"""
    milk_gallons = 3
    milk_ounces = milk_gallons * 128
    milk_ounces -= 13
    result = milk_ounces
    return result

print(solution())