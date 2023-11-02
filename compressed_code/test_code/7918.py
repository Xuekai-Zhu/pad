def solution():
    
    goal_average = 94
    first_four_average = (90 + 98 + 92 + 94) / 4
    fifth_score_needed = (goal_average * 5) - (90 + 98 + 92 + 94)
    result = fifth_score_needed
    return result

print(solution())