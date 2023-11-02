def solution():
    class_size = 30
    min_avg = 75
    pre_william_avg = 74
    william_score_needed = ((class_size+1)*min_avg)-(class_size*pre_william_avg)
    result = william_score_needed
    return result

print(solution())