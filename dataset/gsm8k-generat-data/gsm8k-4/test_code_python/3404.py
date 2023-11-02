def solution():
    """During a school meeting, 300 students and 30 teachers are seated but 25 students are standing. How many attended the school meeting?"""
    # Define the number of seated students and teachers
    seated_students = 300
    seated_teachers = 30

    # Define the number of standing students
    standing_students = 25

    # Calculate the total number of attendees
    total_attendees = seated_students + seated_teachers + standing_students

    result = total_attendees
    return result

print(solution())