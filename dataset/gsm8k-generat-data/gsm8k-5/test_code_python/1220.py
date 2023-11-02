def solution():
    # Height of the first building
    building1 = 600

    # Height of the second building
    building2 = 2 * building1

    # Height of the first and second buildings combined
    building12 = building1 + building2

    # Height of the third building
    building3 = 3 * building12

    # Total height of the three buildings
    total_height = building1 + building2 + building3
    result = total_height
    return result

print(solution())