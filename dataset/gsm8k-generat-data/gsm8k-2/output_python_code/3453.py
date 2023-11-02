def solution():
    """A local college is offering German lessons and currently has 8 students enrolled. Through advertising, 8 more became interested but a fourth of these dropped out within a day. 2 more got frustrated and left. The class then rallied to show how simple the course actually is and increased enrollment by 5 times the amount of students already enrolled in the class, but 2 had to drop it because of scheduling conflicts. After one last rally, 6 more people enrolled. As the days passed, half of the class eventually dropped, and half of the remaining students graduated. How many are still enrolled?"""
    initial_enrollment = 8
    advertising_enrollment = 8
    advertising_dropouts = advertising_enrollment // 4
    current_enrollment = initial_enrollment + advertising_enrollment - advertising_dropouts - 2
    rally_enrollment = current_enrollment * 5
    rally_dropouts = 2
    current_enrollment = rally_enrollment - rally_dropouts + 6
    current_enrollment /= 2
    result = int(current_enrollment)
    return result

print(solution())