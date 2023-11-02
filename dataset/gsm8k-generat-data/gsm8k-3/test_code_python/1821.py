def solution():
    """There are 24 students in the class. One-third had their school portraits taken before lunch. After lunch, but before gym class, 10 additional students had their portraits taken. After gym class, how many students have not yet had their picture taken?"""
    # Define the number of students in the class
    TOTAL_STUDENTS = 24

    # Calculate the number of students who had their portraits taken before lunch
    before_lunch = TOTAL_STUDENTS // 3

    # Calculate the number of students who had their portraits taken after lunch, but before gym class
    after_lunch = before_lunch + 10

    # Calculate the total number of students who have had their portraits taken
    total_taken = before_lunch + after_lunch

    # Calculate the number of students who have not had their portraits taken
    not_taken = TOTAL_STUDENTS - total_taken

    # Display the number of students who have not had their portraits taken
    result = not_taken
    return result

print(solution())