def solution():
    # Set initial weight
    weight = 99

    # Drop a dozen pounds
    weight -= 12

    # Add back twice the initial weight lost
    weight += 2 * 12

    # Drop three times more weight than the initial weight lost
    weight -= 3 * 12

    # Gain back half of a dozen pounds
    weight += 6

    result = weight
    return result

print(solution())