def solution():
    # Convert perfume weight from ounces to pounds
    perfume_weight = 5 * 1.2 / 16
    # Convert soap weight from ounces to pounds
    soap_weight = 2 * 5 / 16
    # Convert jam weight from ounces to pounds
    jam_weight = 2 * 8 / 16

    total_weight = 5 + perfume_weight + 4 + soap_weight + jam_weight
    result = total_weight
    return result

print(solution())