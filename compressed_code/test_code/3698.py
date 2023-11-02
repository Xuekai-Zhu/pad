def solution():
    
    athlete1_total = 26 + 30 + 7
    athlete2_total = 24 + 34 + 8
    athlete1_average = athlete1_total / 3
    athlete2_average = athlete2_total / 3
    if athlete1_average > athlete2_average:
        result = athlete1_average
    else:
        result = athlete2_average
    return result

print(solution())