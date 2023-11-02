def solution():
    class_size = 10  # The size of each class is 10
    total_students = class_size * 2  # The total number of students is twice the class size
    total_chaperones = 5  # 5 parents offered to be chaperones
    total_teachers = 2  # 2 teachers from both classes will be there
    total_people = total_students + total_chaperones + total_teachers  # Total number of people at the zoo
    students_left = 10  # 10 students chose to go home
    parents_left = 2  # 2 of the chaperones were parents who left as well

    # Calculate the number of individuals left at the zoo
    individuals_left = total_people - students_left - parents_left
    result = individuals_left
    return result

print(solution())