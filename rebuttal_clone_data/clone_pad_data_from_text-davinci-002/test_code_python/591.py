def solution():
     pounds_of_cherries = 3
     cherries_per_pound = 80
     cherries_per_minute = 20 / 10
     minutes_per_hour = 60
     total_cherries = pounds_of_cherries * cherries_per_pound
     total_minutes = total_cherries / cherries_per_minute
     total_hours = total_minutes / minutes_per_hour
     result = total_hours
     return result

print(solution())