def solution():
    """There are 400 students in the senior class at East High School. 52% of the students play sports. Of the students that play sports, 12.5% play soccer. How many students play soccer?"""
    # Define the total number of students
    total_students = 400

    # Calculate the number of students who play sports
    sports_students = total_students * 0.52

    # Calculate the number of students who play soccer
    soccer_students = sports_students * 0.125

    # Return the rounded result
    result = round(soccer_students)
    return result

print(solution())