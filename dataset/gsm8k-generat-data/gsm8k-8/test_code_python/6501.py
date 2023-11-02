def solution():
    initial_clothing = 100
    donated1 = 5
    donated2 = donated1 * 3
    thrown_away = 15
    
    remaining_clothing = initial_clothing - donated1 - donated2 - thrown_away
    result = remaining_clothing
    return result

print(solution())