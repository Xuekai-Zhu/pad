def solution():
    """There are 400 students in the senior class at East High School. 52% of the students play sports. Of the students that play sports, 12.5% play soccer. How many students play soccer?"""
    # Number of students in the senior class
    total_students = 400

    # Number of students that play sports
    sports_students = total_students * 0.52

    # Number of students that play soccer
    soccer_students = sports_students * 0.125

    # Display the number of students that play soccer
    result = soccer_students
    return result

print(solution())