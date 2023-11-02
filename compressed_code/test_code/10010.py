def solution():
    
    morning_bundles = 4
    start_bundles = 10
    end_bundles = 3
    afternoon_bundles = start_bundles - morning_bundles - end_bundles
    result = afternoon_bundles
    return result

print(solution())