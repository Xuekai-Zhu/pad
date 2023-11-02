def solution():
     photos_taken_month1 = 146
     days_in_month1 = 31
     photos_taken_month2 = photos_taken_month1 - (days_in_month1 * 2)
     weeks_in_month2 = 4
     photos_taken_week2 = photos_taken_month2 / weeks_in_month2
     result = photos_taken_week2
 
     return result

print(solution())