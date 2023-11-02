def solution():
    boys_ratio = 3
    girls_ratio = 5
    extra_girls = 4

    # Calculate the total number of parts in the ratio
    total_ratio_parts = boys_ratio + girls_ratio

    # Calculate the number of parts for each boy and girl
    boy_parts = boys_ratio / total_ratio_parts
    girl_parts = girls_ratio / total_ratio_parts

    # Calculate the difference in number of parts between boys and girls
    diff_parts = girl_parts - boy_parts

    # Calculate the number of students in the classroom
    total_students = (extra_girls / diff_parts) + 1
    result = total_students
    return result

print(solution())