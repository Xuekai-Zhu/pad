def solution():
    """James has 3 gallons of milk. He drank 13 ounces of the milk. If there are 128 ounces in a gallon, how many ounces of milk does James have left?"""
    # Define the initial amount of milk in ounces
    milk_ounces = 3 * 128

    # Subtract the amount of milk James drank
    milk_ounces -= 13

    # return the result
    result = milk_ounces
    return result

print(solution())