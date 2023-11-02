def solution():
    """Ten percent less than twice the total number of students present in the science class yesterday have attended class today.
    If there were 70 students in the class yesterday and 30 students are absent today, calculate the number of students registered for the course."""

    # Calculate the number of students present today
    present_today = (2 * 70) * 0.9 - 30

    # Calculate the total number of registered students
    registered_students = present_today + 30

    # Display the total number of registered students
    result = registered_students
    return result

print(solution())