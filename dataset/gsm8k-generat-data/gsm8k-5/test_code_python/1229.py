def solution():
    brixton_height = 64  # Zara is 64 inches tall, which is the same as Brixton
    zora_height = brixton_height - 8  # Zora is 8 inches shorter than Brixton
    itzayana_height = zora_height + 4  # Itzayana is 4 inches taller than Zora

    # Calculate the average height of the four people
    average_height = (brixton_height + zora_height + itzayana_height + Zara_height) / 4
    result = average_height
    return result

print(solution())