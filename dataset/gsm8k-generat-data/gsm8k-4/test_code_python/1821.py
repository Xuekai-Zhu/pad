def solution():
    """There are 24 students in the class. One-third had their school portraits taken before lunch. After lunch, but before gym class, 10 additional students had their portraits taken. After gym class, how many students have not yet had their picture taken?"""
    # Define the number of students in the class
    total_students = 24

    # Calculate the number of students who had their portraits taken before lunch
    before_lunch = total_students // 3

    # Calculate the number of students who had their portraits taken after lunch but before gym class
    after_lunch = 10

    # Calculate the number of students who had their portraits taken after gym class
    after_gym = total_students - before_lunch - after_lunch

    # Return the number of students who have not had their picture taken
    result = after_gym
    return result

print(solution())