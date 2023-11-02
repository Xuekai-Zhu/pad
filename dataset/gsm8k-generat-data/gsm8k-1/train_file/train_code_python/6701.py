def solution():
    """There were 100 people in attendance at the school dance. Ten percent of the attendees were school faculty and staff. Of the remaining attendees, two-thirds were girls. How many boys attended the school dance?"""
    total_attendees = 100
    faculty_staff_percent = 10
    faculty_staff_count = total_attendees * (faculty_staff_percent / 100)
    remaining_attendees = total_attendees - faculty_staff_count
    girls_percent = 2/3
    girls_count = remaining_attendees * girls_percent
    boys_count = remaining_attendees - girls_count
    result = boys_count
    return result

print(solution())