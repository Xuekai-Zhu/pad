def solution():
    
    num_goats = 4
    total_carrots = 47
    equal_share = total_carrots // num_goats
    leftover = total_carrots % num_goats
    result = leftover
    return result

print(solution())