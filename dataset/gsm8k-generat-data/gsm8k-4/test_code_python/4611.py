def solution():
    """When the schools were opened for the new year, Hendrix's class had 20 new students. However, at the end of the school year, 1/3 of the students in Hendrix class had transferred to other schools. If the number of students that were in Hendrix's class before 20 new students joined was 160, calculate the number of students that were in the class at the end of the year."""
    # Define the initial number of students in Hendrix's class
    initial_students = 160

    # Calculate the number of students who joined the class during the year
    new_students = 20

    # Calculate the total number of students in Hendrix's class
    total_students = initial_students + new_students

    # Calculate the number of students who transferred to other schools
    transfers = total_students / 3

    # Calculate the number of students who remained in Hendrix's class at the end of the year
    remaining_students = total_students - transfers

    # return the result
    result = remaining_students
    return result

print(solution())