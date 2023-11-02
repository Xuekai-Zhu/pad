def solution():
     number_of_squats = 30
     number_of_days = 4
     number_of_squats_increase = 5
     total_number_of_squats = number_of_squats + (number_of_days * number_of_squats_increase)
     day_after_tomorrow = total_number_of_squats + 5
     result = day_after_tomorrow
     return result

print(solution())