def solution():
    
    adam_points = 50
    betty_points = adam_points * 1.3
    martha_points = betty_points * 3
    tom_points = tom_points - 30
    total_points = adam_points + betty_points + martha_points + 400
    missing_points = total_points - 400
    result = missing_points
    return result

print(solution())