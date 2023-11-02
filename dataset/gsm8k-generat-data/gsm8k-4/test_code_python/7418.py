def solution():
    """Josh found out that 7 bottle caps weigh exactly one ounce. Josh's entire bottle cap collection weighs 18 pounds exactly. How many bottle caps does Josh have in his collection?"""
    # Define the weight of 1 bottle cap in ounces and the weight of Josh's collection in pounds
    WEIGHT_PER_BOTTLE_CAP = 1/7
    WEIGHT_OF_COLLECTION = 18 * 16  # 18 pounds converted to ounces

    # Calculate the number of bottle caps in Josh's collection
    num_bottle_caps = WEIGHT_OF_COLLECTION / WEIGHT_PER_BOTTLE_CAP

    # Round the number of bottle caps to the nearest whole number
    rounded_num_bottle_caps = round(num_bottle_caps)

    # return the result
    result = rounded_num_bottle_caps
    return result

print(solution())