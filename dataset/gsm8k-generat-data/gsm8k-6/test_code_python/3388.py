def solution():
    # Calculate the total weight of the perfume bottles in pounds
    perfume_weight = 5 * 1.2 / 16  

    # Calculate the total weight of the soap bars in pounds
    soap_weight = 2 * 5 / 16

    # Calculate the total weight of the jam jars in pounds
    jam_weight = 2 * 8 / 16

    # Calculate the total weight of all items in pounds
    total_weight = 5 + perfume_weight + 4 + soap_weight + jam_weight

    result = total_weight
    return result

print(solution())