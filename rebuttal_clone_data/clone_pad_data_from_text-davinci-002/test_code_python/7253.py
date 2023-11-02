def solution():
     morning_red_chairs = 4
     morning_yellow_chairs = morning_red_chairs * 2
     morning_blue_chairs = morning_yellow_chairs - 2
     afternoon_borrowed_chairs = 3
     afternoon_remaining_chairs = morning_red_chairs + morning_yellow_chairs + morning_blue_chairs - afternoon_borrowed_chairs
     result =  afternoon_remaining_chairs
     return result

print(solution())