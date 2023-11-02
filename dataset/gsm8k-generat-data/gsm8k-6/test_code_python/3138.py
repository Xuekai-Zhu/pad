def solution():
    grades = [2, 2, 2, 3, 3, 3, 3, 4, 5]  # Milo's grades
    average_grade = sum(grades) / len(grades)  # Calculate the average of Milo's grades
    cash_reward = 5 * average_grade  # Calculate the cash reward based on the average grade
    result = cash_reward
    return result

print(solution())