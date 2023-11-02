def solution():
     minutes_studying_science = 60
     minutes_studying_math = 80
     minutes_studying_literature = 40
     total_minutes_studying = minutes_studying_science + minutes_studying_math + minutes_studying_literature
     total_hours_studying = total_minutes_studying / 60
     result = total_hours_studying
     return result

print(solution())