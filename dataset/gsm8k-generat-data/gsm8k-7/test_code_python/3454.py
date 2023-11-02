def solution():
    initial_enrollment = 8
    new_interest = 8
    new_dropouts = new_interest / 4
    new_enrollment = new_interest - new_dropouts
    frustration_dropouts = 2
    rally_multiplier = 5
    rally_enrollment = initial_enrollment * rally_multiplier
    scheduling_dropouts = 2
    final_enrollment = rally_enrollment + 6 - scheduling_dropouts
    half_dropouts = final_enrollment / 2
    remaining_students = final_enrollment - half_dropouts / 2
    result = remaining_students
    return result

print(solution())