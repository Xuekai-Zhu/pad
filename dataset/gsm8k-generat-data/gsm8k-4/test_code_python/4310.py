def solution():
    """Ten percent less than twice the total number of students present in the science class yesterday have attended class today. If there were 70 students in the class yesterday and 30 students are absent today, calculate the number of students registered for the course."""
    # Calculate the number of students present in the class today
    present_today = (0.9 * 2 * 70) - 30

    # Calculate the total number of students registered for the course
    total_registered = present_today + 30

    # return the result
    result = total_registered
    return result

print(solution())