def solution():
    oysters_day_one = 50
    crabs_day_one = 72
    oysters_day_two = oysters_day_one / 2
    crabs_day_two = crabs_day_one / 3
    total_oysters = oysters_day_one + oysters_day_two
    total_crabs = crabs_day_one + crabs_day_two
    result = (total_oysters, total_crabs)
    
    return result

print(solution())