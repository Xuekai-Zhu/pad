def solution():
    suitcase_weight = 5  # in pounds
    perfume_weight = 5 * 1.2 / 16  # in pounds
    chocolate_weight = 4
    soap_weight = 2 * 5 / 16  # in pounds
    jam_weight = 2 * 8 / 16  # in pounds

    # Calculate the total weight of all items Jacque picked up
    total_picked_up_weight = perfume_weight + chocolate_weight + soap_weight + jam_weight

    # Calculate the total weight of Jacque's suitcase on the return flight
    total_weight = suitcase_weight + total_picked_up_weight
    result = total_weight
    return result

print(solution())