def solution():
    
    total_attendees = 100
    faculty_staff = total_attendees * 0.1
    remaining_attendees = total_attendees - faculty_staff
    girls = remaining_attendees * (2/3)
    boys = remaining_attendees - girls
    result = boys
    return result

print(solution())