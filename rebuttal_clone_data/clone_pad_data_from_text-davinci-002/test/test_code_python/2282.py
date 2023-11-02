def solution():
    boxes_bought = 14
    packets_bought = 15
    boxes_needed = 2
    packets_needed = 3
    Oreo_cheesecakes = packets_bought // packets_needed
    Graham_crackers_leftover = boxes_bought - (Oreo_cheesecakes * boxes_needed)
    result = Graham_crackers_leftover
    return result

print(solution())