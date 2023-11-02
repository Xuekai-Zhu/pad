def solution():
    # Calculate the number of students that transferred to other schools
    transferred_students = (1/3) * 180  # assuming the class ended up with 180 students after 20 new students joined

    # Calculate the number of students that remained
    remaining_students = 180 - transferred_students

    result = remaining_students
    return result

print(solution())