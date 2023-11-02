def solution():
    
    grades = [2, 2, 2, 3, 3, 3, 3, 4, 5]
    average_grade = sum(grades) / len(grades)
    cash_reward = 5 * average_grade
    result = cash_reward
    return result

print(solution())