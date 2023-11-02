def solution():
    total_shells = 65
    purple_shells = 13
    pink_shells = 8
    yellow_shells = 18
    blue_shells = 12
    orange_shells = total_shells - purple_shells - pink_shells - yellow_shells - blue_shells
    result = orange_shells
    
    return result

print(solution())