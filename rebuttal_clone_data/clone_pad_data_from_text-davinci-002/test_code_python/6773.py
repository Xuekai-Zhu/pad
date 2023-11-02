def solution():
     total_tips_earned = 145
     number_of_nights = 5
     average_per_night = 50
     total_needed = average_per_night * number_of_nights - total_tips_earned
     result = total_needed
     return result

print(solution())