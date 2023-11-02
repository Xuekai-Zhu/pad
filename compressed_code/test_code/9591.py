def solution():
    
    previous_property = 2
    new_property = previous_property * 10
    land_not_suitable = 1
    land_suitable = new_property - land_not_suitable
    result = land_suitable
    return result

print(solution())