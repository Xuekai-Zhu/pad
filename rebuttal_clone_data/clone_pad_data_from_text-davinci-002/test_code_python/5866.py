def solution():
    graduates = 50
    parents = graduates * 2
    teachers = 20
    administrators = teachers / 2
    total_attendees = parents + teachers + administrators
    chairs_needed = total_attendees
    result = chairs_needed
    return result

print(solution())