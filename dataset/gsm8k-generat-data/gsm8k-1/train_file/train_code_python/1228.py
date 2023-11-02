def solution():
    """Itzayana is 4 inches taller than Zora, who is 8 inches shorter than Brixton. If Zara is 64 inches tall and has the same height as Brixton, calculate the average height of the four people."""
    zara_height = 64
    brixton_height = zara_height
    zora_height = brixton_height - 8
    itzayana_height = zora_height + 4
    total_height = zara_height + brixton_height + zora_height + itzayana_height
    average_height = total_height / 4
    result = average_height
    return result

print(solution())