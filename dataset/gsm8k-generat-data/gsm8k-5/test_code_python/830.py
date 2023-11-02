def solution():
    total_students = 100  # Let's assume 100 students for simplicity
    home_learning_students = 0.4 * total_students  # Forty percent of students are learning from home
    in_school_students = 0.3 * total_students  # Remaining students are divided into two equal groups, only one in school on any day
    percent_in_school = (in_school_students / total_students) * 100  # Calculate the percent of students in school
    result = percent_in_school
    return result

print(solution())