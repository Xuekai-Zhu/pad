def solution():
     money_earned = 6
     money_needed = 340
     money_saved = 40
     days_per_week = 5
     money_to_be_saved = money_needed - money_saved
     days_needed = money_to_be_saved / money_earned
     weeks_needed = days_needed / days_per_week
     result = weeks_needed
 
     return result

print(solution())