def solution():
     piano_cost = 500
     initial_lesson_cost = 40
     discount = 25
     final_lesson_cost = initial_lesson_cost - (initial_lesson_cost * (discount / 100))
     total_lesson_cost = final_lesson_cost * 20
     total_cost = total_lesson_cost + piano_cost
     result = total_cost
 
     return result

print(solution())