def solution():
    """There are 32 students in a statistics course.  25 percent of the class received an A.  1/4 of the remaining students got either a B or C, and the rest of the students failed.  How many students failed?"""
    # Define the number of students in the class and the percentage that received an A
    total_students = 32
    a_percent = 25

    # Calculate the number of students who received an A
    a_count = int(total_students * a_percent / 100)

    # Calculate the number of students who did not receive an A
    remaining_count = total_students - a_count

    # Calculate the number of students who got a B or C
    b_c_count = remaining_count // 4

    # Calculate the number of students who failed
    fail_count = total_students - (a_count + b_c_count)

    # Display the number of students who failed
    result = fail_count
    return result

print(solution())