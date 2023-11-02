def solution():
    """A local college is offering German lessons and currently has 8 students enrolled. Through advertising, 8 more became interested but a fourth of these dropped out within a day. 2 more got frustrated and left. The class then rallied to show how simple the course actually is and increased enrollment by 5 times the amount of students already enrolled in the class, but 2 had to drop it because of scheduling conflicts. After one last rally, 6 more people enrolled. As the days passed, half of the class eventually dropped, and half of the remaining students graduated. How many are still enrolled?"""
    initial_enrollment = 8
    new_enrollment = 8 * 3 / 4
    frustrated = 2
    total_enrollment = initial_enrollment + new_enrollment - frustrated
    total_enrollment *= 5
    total_enrollment -= 2
    total_enrollment += 6
    total_enrollment /= 2
    total_enrollment /= 2
    result = total_enrollment
    return result

print(solution())