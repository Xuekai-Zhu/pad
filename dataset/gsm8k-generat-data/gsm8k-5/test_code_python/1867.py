def solution():
    num_students = 20  # There are 20 students in the class
    num_students_in_classroom = num_students // 4  # One-fourth of the students stayed in the classroom
    num_students_on_playground = num_students - num_students_in_classroom  # The rest went to the playground
    num_boys_on_playground = num_students_on_playground // 3  # One-third of the students on the playground are boys
    num_girls_on_playground = num_students_on_playground - num_boys_on_playground  # The rest are girls

    result = num_girls_on_playground
    return result

print(solution())