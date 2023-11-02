def solution():
    
    total_goldfish = 100
    allowed_goldfish = total_goldfish / 2
    caught_goldfish = 3/5 * allowed_goldfish
    remaining_goldfish = allowed_goldfish - caught_goldfish
    result = remaining_goldfish
    return result

print(solution())