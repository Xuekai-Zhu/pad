def solution():
     total_attendees = 100
     faculty_and_staff = 10
     remaining_attendees = total_attendees - faculty_and_staff
     girls = remaining_attendees * (2/3)
     boys = remaining_attendees - girls
     result = boys
     return result

print(solution())