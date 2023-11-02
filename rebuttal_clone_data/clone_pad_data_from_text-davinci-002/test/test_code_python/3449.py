def solution():
    boxes_opened = 12
    samples_leftover = 5
    samples_used = boxes_opened * 20 - samples_leftover
    result = samples_used
    return result

print(solution())