def solution():
    """Mr. Angstadt has 120 students throughout the school day.  Half of them are enrolled in Statistics.  Of the students in Statistics, 90 percent are seniors.  How many of Mr. Angstadt's students are seniors enrolled in Statistics?"""
    # Define the total number of students
    total_students = 120

    # Calculate the number of students enrolled in Statistics
    stats_students = total_students / 2

    # Calculate the number of senior students in Statistics
    senior_stats_students = stats_students * 0.9

    # Display the number of senior students in Statistics
    result = senior_stats_students
    return result

print(solution())