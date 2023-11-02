def solution():
     chess_hours = 2
     drama_hours = 8
     glee_hours = 3
     weeks_in_semester = 12
     weeks_sick = 2
     weeks_left = weeks_in_semester - weeks_sick
     hours_per_week_left = chess_hours + drama_hours + glee_hours
     total_hours = hours_per_week_left * weeks_left
     result = total_hours
     return result

print(solution())