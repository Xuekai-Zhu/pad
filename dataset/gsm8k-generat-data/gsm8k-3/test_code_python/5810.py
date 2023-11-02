def solution():
    """There are 64 seventh graders at a middle school. This is 32% of the students at the school. The sixth graders comprise 38% of the students. How many sixth graders attend middle school?"""
    # Define the number of seventh graders and the percentage of students they represent
    seventh_graders = 64
    seventh_percentage = 0.32

    # Calculate the total number of students
    total_students = seventh_graders / seventh_percentage

    # Calculate the number of sixth graders
    sixth_percentage = 0.38
    sixth_graders = total_students * sixth_percentage

    # Display the number of sixth graders
    result = sixth_graders
    return result

print(solution())