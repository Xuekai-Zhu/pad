def solution():
     homework_time_minutes = 150
     math_time_percentage = 30
     science_time_percentage = 40
     other_subjects_time_percentage = 100 - math_time_percentage - science_time_percentage
     other_subjects_time_minutes = homework_time_minutes * (other_subjects_time_percentage / 100)
     result = other_subjects_time_minutes
     return result

print(solution())