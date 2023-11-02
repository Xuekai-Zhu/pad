def solution():
    """There were 100 people in attendance at the school dance.  Ten percent of the attendees were school faculty and staff.  Of the remaining attendees, two-thirds were girls.  How many boys attended the school dance?"""
    # Calculate number of faculty and staff attendees
    faculty_staff = int(0.1 * 100)

    # Calculate number of non-faculty/staff attendees
    non_faculty_staff = 100 - faculty_staff

    # Calculate number of girls among non-faculty/staff attendees
    girls = int((2/3) * non_faculty_staff)

    # Calculate number of boys among non-faculty/staff attendees
    boys = non_faculty_staff - girls

    # Display number of boys
    result = boys
    return result

print(solution())