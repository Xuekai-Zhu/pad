def solution():
    
    graduate_count = 50
    parent_count = graduate_count * 2
    teacher_count = 20
    admin_count = teacher_count / 2
    total_attendees = graduate_count + parent_count + teacher_count + admin_count
    total_chairs = total_attendees
    result = total_chairs
    return result

print(solution())