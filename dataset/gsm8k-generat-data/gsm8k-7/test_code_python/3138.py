def solution():
    grades = [2, 2, 2, 3, 3, 3, 3, 4, 5]
    num_grades = len(grades)

    # Calculate the average grade
    avg_grade = sum(grades) / num_grades

    # Calculate the cash reward Milo will receive
    cash_reward = avg_grade * 5
    result = cash_reward
    return result

print(solution())