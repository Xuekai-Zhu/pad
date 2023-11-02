def solution():
    
    kylie_towels = 3
    daughters_towels = 6
    husband_towels = 3
    total_towels = kylie_towels + daughters_towels + husband_towels
    loads = total_towels // 4
    if total_towels % 4 != 0:
        loads += 1
    result = loads
    return result

print(solution())