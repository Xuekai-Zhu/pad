def solution():
    """When the schools were opened for the new year, Hendrix's class had 20 new students. However, at the end of the school year, 1/3 of the students in Hendrix class had transferred to other schools. If the number of students that were in Hendrix's class before 20 new students joined was 160, calculate the number of students that were in the class at the end of the year."""
    initial_students = 160
    new_students = 20
    transferred_students = initial_students / 3
    remaining_students = initial_students + new_students - transferred_students
    result = remaining_students
    return result

print(solution())