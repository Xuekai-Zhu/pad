def solution():
    
    normal_temp = 95
    sickness_temp = 10
    new_temp = normal_temp + sickness_temp
    fever_threshold = 100
    above_fever_threshold = new_temp - fever_threshold
    result = above_fever_threshold
    return result

print(solution())