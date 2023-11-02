def solution():
     total_collected = 20
     weekly_contribution = 10
     total_needed = 120
     number_of_weeks = (total_needed - total_collected) / weekly_contribution
     result = number_of_weeks
     return result

print(solution())