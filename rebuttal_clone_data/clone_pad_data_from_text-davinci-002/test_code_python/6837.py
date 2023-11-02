def solution():
    original_crayons = 21
    crayons_in_locker = 36
    crayons_from_friend = original_crayons / 2
    total_crayons = original_crayons + crayons_in_locker + crayons_from_friend
    crayons_for_sister = total_crayons / 3
    result = crayons_for_sister
    
    return result

print(solution())