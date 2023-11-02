def solution():
    # Calculate the average grade
    total_grades = 3*2 + 4*3 + 4 + 5  # Milo gets three 2s, four 3s, a 4, and a 5
    average_grade = total_grades / 9

    # Calculate the cash reward
    cash_reward = 5 * average_grade
    result = cash_reward
    return result

print(solution())