def solution():
    # Calculate the number of boys at the dance
    girls_ratio = 4/7  # ratio of girls to total students
    total_students = 60/girls_ratio  # total number of students at the dance
    boys_ratio = 3/7  # ratio of boys to total students
    boys = boys_ratio * total_students  # number of boys at the dance

    # Calculate the number of teachers at the dance
    teacher_ratio = 20/100  # ratio of teachers to boys
    teachers = teacher_ratio * boys  # number of teachers at the dance

    # Calculate the total number of people at the dance
    total_people = total_students + teachers
    result = total_people
    return result

print(solution())