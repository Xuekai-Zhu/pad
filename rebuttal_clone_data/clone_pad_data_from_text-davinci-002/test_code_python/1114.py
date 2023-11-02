def solution():
     donuts_made = 10
     days_worked = 12
     donuts_eaten = 1
     donuts_given_away = 8
     donuts_left = donuts_made - donuts_eaten - donuts_given_away
     donuts_per_box = 10
     boxes_filled = donuts_left / donuts_per_box
     result = boxes_filled
    
     return result

print(solution())