def solution():
    total_students = 25
    absent_student = 1
    average_score = 77
    present_students = total_students - absent_student
    pizza_party_threshold = 75
    
    # the average score must be greater than 75%
    # so the sum of all the scores must be greater than 
    # (75% of 25 students) * 100
    required_score = (pizza_party_threshold / 100) * (total_students * 100)
    
    # the sum of all the scores is the average score times the number of present students
    # so the lowest score the absent student can get is the required score minus the sum of all the scores
    lowest_score = required_score - (present_students * average_score)
    
    result = lowest_score
    
    return result

print(solution())