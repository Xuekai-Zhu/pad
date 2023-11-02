def solution():
    
    total_people = 6000
    graduates = 950
    faculty_attendees = 300
    total_attendees = graduates + faculty_attendees
    tickets_per_graduate = total_attendees / total_people
    result = tickets_per_graduate
    return result

print(solution())