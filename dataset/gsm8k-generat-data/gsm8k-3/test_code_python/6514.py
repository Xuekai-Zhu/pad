def solution():
    """There are 500 students in a local high school.  40 percent are juniors.  70 percent of juniors are involved in sports.  How many juniors are involved in sports?"""
    # Define the number of students and the percentage of juniors and juniors involved in sports
    TOTAL_STUDENTS = 500
    JUNIOR_PERCENTAGE = 0.4
    JUNIOR_SPORTS_PERCENTAGE = 0.7

    # Calculate the number of junior students
    junior_students = TOTAL_STUDENTS * JUNIOR_PERCENTAGE

    # Calculate the number of junior students involved in sports
    junior_sports_students = junior_students * JUNIOR_SPORTS_PERCENTAGE

    # Display the number of junior students involved in sports
    result = junior_sports_students
    return result

print(solution())