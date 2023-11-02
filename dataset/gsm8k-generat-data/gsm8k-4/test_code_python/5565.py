def solution():
    """Mr. Angstadt has 120 students throughout the school day. Half of them are enrolled in Statistics. Of the students in Statistics, 90 percent are seniors. How many of Mr. Angstadt's students are seniors enrolled in Statistics?"""
    # Define the total number of students and the percentage enrolled in Statistics
    total_students = 120
    stat_percentage = 0.5

    # Calculate the number of students enrolled in Statistics and the number of seniors in Statistics
    stat_students = total_students * stat_percentage
    senior_stat_students = stat_students * 0.9

    # Return the result
    result = senior_stat_students
    return result

print(solution())