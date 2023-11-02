def solution():
    total_students = 50
    free_lunch_students = total_students * 0.4
    cost_per_meal = 210
    total_cost = cost_per_meal * total_students
    paying_students = total_students - free_lunch_students
    cost_per_paying_student = total_cost / paying_students
    result = cost_per_paying_student
    return result

print(solution())