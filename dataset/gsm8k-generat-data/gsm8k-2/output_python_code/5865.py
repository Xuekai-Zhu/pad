def solution():
    """In a graduation ceremony, each graduate can bring their 2 parents. Twenty teachers and half as many administrators will also attend the graduation ceremony. If there are 50 graduates, how many chairs must be prepared for the ceremony?"""
    graduate_count = 50
    parent_count = graduate_count * 2
    teacher_count = 20
    admin_count = teacher_count / 2
    total_attendees = graduate_count + parent_count + teacher_count + admin_count
    total_chairs = total_attendees
    result = total_chairs
    return result

print(solution())