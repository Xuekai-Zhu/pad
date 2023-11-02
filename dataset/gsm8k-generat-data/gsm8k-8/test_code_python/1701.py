def solution():
    total_weight = 120
    applesauce_weight = total_weight / 2
    remaining_weight = total_weight - applesauce_weight
    pies_weight = remaining_weight
    pies_count = pies_weight / 4
    result = pies_count
    return result

print(solution())