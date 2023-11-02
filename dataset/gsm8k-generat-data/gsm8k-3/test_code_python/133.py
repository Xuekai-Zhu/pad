def solution():
    """There are 40 students in a class. If 1/10 are absent, 3/4 of the students who are present are in the classroom, and the rest are in the canteen, how many students are in the canteen?"""
    # Define the number of students in the class
    total_students = 40

    # Calculate the number of absent students
    absent_students = total_students // 10

    # Calculate the number of present students
    present_students = total_students - absent_students

    # Calculate the number of students in the classroom
    classroom_students = present_students * 3/4

    # Calculate the number of students in the canteen
    canteen_students = present_students - classroom_students

    # return the result
    result = canteen_students
    return result

print(solution())