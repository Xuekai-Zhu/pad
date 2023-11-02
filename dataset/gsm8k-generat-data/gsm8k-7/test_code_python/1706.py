def solution():
    num_students = 400
    sports_percentage = 0.52
    soccer_percentage = 0.125

    # Calculate the number of students that play sports
    num_sports_students = num_students * sports_percentage

    # Calculate the number of students that play soccer
    num_soccer_students = num_sports_students * soccer_percentage
    result = num_soccer_students
    return result

print(solution())