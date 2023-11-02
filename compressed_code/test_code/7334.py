def solution():
    
    num_problems = 20
    time_with_calc = num_problems * 2
    time_without_calc = num_problems * 5
    time_saved = time_without_calc - time_with_calc
    result = time_saved
    return result

print(solution())