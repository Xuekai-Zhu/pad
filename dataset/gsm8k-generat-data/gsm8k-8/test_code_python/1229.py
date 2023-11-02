def solution():
    brixton_height = 64
    zora_height = brixton_height - 8
    itzayana_height = zora_height + 4
    total_height = brixton_height + zora_height + itzayana_height + 64
    average_height = total_height / 4
    result = average_height
    return result

print(solution())