def solution():
    # Calculate the total number of original plates
    original_plates = 4 + 8

    # Calculate the number of new polka dotted plates Jack buys
    new_plates = 2 * 8

    # Subtract one smashed flowered plate from the total number of plates
    total_plates = original_plates + new_plates - 1

    result = total_plates
    return result

print(solution())