def solution():
     weeks_in_semester = 15
     weekdays_in_semester = weeks_in_semester * 5
     hours_studied_weekdays = weekdays_in_semester * 3
     weekends_in_semester = weeks_in_semester * 2
     hours_studied_weekends = (weekends_in_semester * 4) + (weekends_in_semester * 5)
     total_hours_studied = hours_studied_weekdays + hours_studied_weekends 
     result = total_hours_studied
     return result

print(solution())