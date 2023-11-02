def solution():
    zara_height = 64
    brixton_height = zara_height
    zora_height = brixton_height - 8
    itzayana_height = zora_height + 4

    # Calculate the total height of all four people
    total_height = zara_height + brixton_height + zora_height + itzayana_height

    # Calculate the average height of all four people
    average_height = total_height / 4
    result = average_height
    return result

print(solution())