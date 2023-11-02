def solution():
    # Calculate Zora's height
    zora_height = 64 - 8

    # Calculate Itzayana's height
    itzayana_height = zora_height + 4

    # Calculate the total height of the four people
    total_height = zora_height + itzayana_height + 64 + 64

    # Calculate the average height
    average_height = total_height / 4
    result = average_height
    return result

print(solution())