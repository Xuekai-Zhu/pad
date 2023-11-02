def solution():
    # Define the percentage of students learning from home
    home_learning_percentage = 40

    # Calculate the percentage of students attending school
    school_attendance_percentage = (100 - home_learning_percentage) / 2
    result = school_attendance_percentage
    return result

print(solution())