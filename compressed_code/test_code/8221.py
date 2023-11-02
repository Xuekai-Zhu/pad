def solution():
    
    oranges = 50
    oranges_limes_ratio = 2
    limes = oranges / oranges_limes_ratio
    remaining_fruits = oranges + limes
    initially_had = remaining_fruits * 2
    result = initially_had
    return result

print(solution())