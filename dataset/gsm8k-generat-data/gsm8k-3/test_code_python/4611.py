def solution():
    """When the schools were opened for the new year, Hendrix's class had 20 new students. However, at the end of the school year, 1/3 of the students in Hendrix class had transferred to other schools. If the number of students that were in Hendrix's class before 20 new students joined was 160, calculate the number of students that were in the class at the end of the year."""
    # Calculate the number of students in Hendrix's class after new students joined
    students = 160 + 20

    # Calculate the number of students who transferred out of Hendrix's class
    transferred = students // 3

    # Calculate the number of students remaining in Hendrix's class
    remaining = students - transferred

    # Display the number of students at the end of the year
    result = remaining
    return result

print(solution())