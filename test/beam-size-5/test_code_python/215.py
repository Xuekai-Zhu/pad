def solution():
    
    total_points = 251
    naomi_points = 68
    yuri_points = (naomi_points / 2) + 10
    brianna_points = naomi_points + 17
    joj_points = total_points - naomi_points - yuri_points - brianna_points
    result = joj_points
    return result

print(solution())