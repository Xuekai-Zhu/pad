def solution():
    
    day_1_oysters = 50
    day_1_crabs = 72
    day_2_oysters = day_1_oysters / 2
    day_2_crabs = day_1_crabs * (2/3)
    total_oysters = day_1_oysters + day_2_oysters
    total_crabs = day_1_crabs + day_2_crabs
    result = total_oysters + total_crabs
    return result

print(solution())