def solution():
    """Forty percent of the students have elected to learn from home during the pandemic. The remaining students are divided into two equal groups, only one of which is physically in school on any day. What percent of students are present in school?"""
    # Define the percentage of students learning from home
    home_learning_percentage = 40

    # Calculate the percentage of students physically attending school
    school_attendance_percentage = (100 - home_learning_percentage) / 2

    # Return the result
    result = school_attendance_percentage
    return result

print(solution())