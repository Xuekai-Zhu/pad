def solution():
    """The number of students in a school hall was 1000. The hall had 3 entrances A, B, and C which also served as the exits. If after a meeting 30% of the students went out of the building through exit A, 3/5 of the remaining went out through exit B, and the rest went out through exit C, calculate the number of students who went out through exit C."""
    total_students = 1000
    exit_a = int(0.3 * total_students)
    remaining_students = total_students - exit_a
    exit_b = int(0.6 * remaining_students)
    exit_c = remaining_students - exit_b
    result = exit_c
    return result

print(solution())