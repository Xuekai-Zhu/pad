def solution():
    bonus = 500
    extra_bonus = 10
    average_needed = 75
    tests_graded = 8
    average_so_far = 70
    max_score = 150
    total_needed = ((average_needed * (tests_graded + 2)) - (max_score * tests_graded)) / 2
    result = total_needed + (bonus + (extra_bonus * 2)) 
    return result

print(solution())