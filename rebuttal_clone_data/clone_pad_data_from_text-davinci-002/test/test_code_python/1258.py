def solution():
     minutes_in_an_hour = 60
     lessons_on_monday = 6
     lessons_on_tuesday = 3
     lessons_on_wednesday = lessons_on_tuesday * 2
     minutes_on_monday = lessons_on_monday * 30
     minutes_on_tuesday = lessons_on_tuesday * minutes_in_an_hour
     minutes_on_wednesday = lessons_on_wednesday * minutes_in_an_hour
     total_minutes = minutes_on_monday + minutes_on_tuesday + minutes_on_wednesday
     total_hours = total_minutes / minutes_in_an_hour
     result = total_hours
 
     return result

print(solution())