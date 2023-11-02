def solution():
    """A local college is offering German lessons and currently has 8 students enrolled. Through advertising, 8 more became interested but a fourth of these dropped out within a day. 2 more got frustrated and left. The class then rallied to show how simple the course actually is and increased enrollment by 5 times the amount of students already enrolled in the class, but 2 had to drop it because of scheduling conflicts. After one last rally, 6 more people enrolled. As the days passed, half of the class eventually dropped, and half of the remaining students graduated. How many are still enrolled?"""
    # Define the initial number of students
    initial_students = 8

    # Calculate the number of students after the first round of advertising
    new_students = 8
    new_dropouts = new_students // 4
    new_students -= new_dropouts
    new_dropouts += 2
    total_students = initial_students + new_students - new_dropouts

    # Calculate the number of students after the second round of advertising
    new_students = total_students * 5
    new_dropouts = 2
    total_students += new_students - new_dropouts

    # Calculate the number of students after the third round of advertising
    new_students = 6
    total_students += new_students

    # Calculate the number of students after half drop out
    total_students //= 2

    # Calculate the number of students remaining after half of the remaining students graduate
    total_students //= 2

    # Display the number of students still enrolled
    result = total_students
    return result

print(solution())