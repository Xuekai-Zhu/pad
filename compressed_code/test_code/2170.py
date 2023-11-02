def solution():
    
    bottle_size = 20
    bottles_per_day = 3
    total_bottles = bottles_per_day * 7
    total_ounces = total_bottles * bottle_size
    total_ounces -= 5 + 8
    result = total_ounces
    return result

print(solution())