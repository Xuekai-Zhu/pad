def solution():
    class_size = 32  # There are 32 students in the course
    percent_a = 25  # 25 percent of the class received an A
    a_students = int(class_size * percent_a / 100)  # Calculate how many students received an A
    remaining_students = class_size - a_students  # Calculate how many students remain

    # Calculate how many students received a B or C
    b_or_c_students = int(remaining_students / 4)
    # Calculate how many students failed
    failed_students = remaining_students - b_or_c_students

    result = failed_students
    return result

print(solution())