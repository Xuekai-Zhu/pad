def solution():
    # Calculate how many students are absent
    restroom_count = 2
    absent_count = 3 * restroom_count - 1

    # Calculate how many students are in the classroom
    desk_count = 4 * 6
    filled_desks = desk_count * 2/3
    classroom_count = filled_desks + restroom_count

    # Calculate the total number of students
    total_count = classroom_count + absent_count
    result = total_count
    return result

print(solution())