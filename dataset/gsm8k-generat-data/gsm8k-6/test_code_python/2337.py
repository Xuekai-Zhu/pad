def solution():
    # Calculate the total cost of shirts for each grade
    cost_kindergarten = 101 * 5.8
    cost_first_grade = 113 * 5
    cost_second_grade = 107 * 5.6
    cost_third_grade = 108 * 5.25

    # Calculate the total cost of shirts for all grades
    total_cost = cost_kindergarten + cost_first_grade + cost_second_grade + cost_third_grade
    result = total_cost
    return result

print(solution())