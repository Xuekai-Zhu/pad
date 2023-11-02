def solution():
    
    normal_temp = 95
    sick_temp = normal_temp + 10
    fever_threshold = 100
    degrees_above_fever = sick_temp - fever_threshold
    result = degrees_above_fever if degrees_above_fever > 0 else 0
    return result

print(solution())