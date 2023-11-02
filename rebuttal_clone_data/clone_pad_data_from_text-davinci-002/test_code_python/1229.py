def solution():
    zora_height = 64
    brixton_height = zora_height
    difference1 = zora_height - brixton_height
    difference2 = difference1 - 8
    itzayana_height = difference2 + 4
    total_height = itzayana_height + zora_height + brixton_height
    average_height = total_height / 4
    result = average_height
    return result

print(solution())