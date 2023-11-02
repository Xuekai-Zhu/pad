def solution():
    """A local college is offering German lessons and currently has 8 students enrolled. Through advertising, 8 more became interested but a fourth of these dropped out within a day. 2 more got frustrated and left. The class then rallied to show how simple the course actually is and increased enrollment by 5 times the amount of students already enrolled in the class, but 2 had to drop it because of scheduling conflicts. After one last rally, 6 more people enrolled. As the days passed, half of the class eventually dropped, and half of the remaining students graduated. How many are still enrolled?"""
    # Initialize the number of enrolled students to the current number
    enrolled_students = 8

    # Calculate the number of students who dropped out after the first advertising
    dropped_first = 8 * 0.25

    # Update the number of enrolled students
    enrolled_students += (8 - dropped_first) - 2

    # Calculate the number of students who enrolled after the rally
    enrolled_rally = enrolled_students * 5

    # Update the number of enrolled students
    enrolled_students += enrolled_rally - 2 + 6

    # Calculate the number of students who dropped out
    dropped_out = enrolled_students * 0.5

    # Calculate the number of remaining students
    remaining_students = enrolled_students - dropped_out

    # Calculate the number of students who graduated
    graduated_students = remaining_students * 0.5

    # Calculate the final number of enrolled students
    enrolled_students_final = remaining_students - graduated_students

    result = enrolled_students_final
    return result

print(solution())