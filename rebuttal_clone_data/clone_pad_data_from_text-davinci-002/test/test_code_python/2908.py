def solution():
     cost_per_lesson = 30
     hours_per_lesson = 1.5
     number_of_hours = 18
     number_of_lessons = number_of_hours / hours_per_lesson
     total_cost = cost_per_lesson * number_of_lessons
     result = total_cost
     return result

print(solution())