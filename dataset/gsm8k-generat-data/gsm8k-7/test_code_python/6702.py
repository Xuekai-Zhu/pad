def solution():
    total_attendees = 100
    faculty_staff_percent = 0.1
    girls_percent = 2/3

    # Calculate the number of attendees who were faculty and staff
    faculty_staff_count = total_attendees * faculty_staff_percent

    # Calculate the number of attendees who were not faculty or staff
    non_faculty_staff_count = total_attendees - faculty_staff_count

    # Calculate the number of girls in attendance
    girls_count = non_faculty_staff_count * girls_percent

    # Calculate the number of boys in attendance
    boys_count = non_faculty_staff_count - girls_count
    result = boys_count
    return result

print(solution())