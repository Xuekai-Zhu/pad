def solution():
    """The average GPA for 6th graders is 93, the 7th graders is 2 more than the 6th graders and the 8th graders average GPA is 91.  What is the average GPA for the school?"""
    # Define the average GPA for each grade level
    GPA_6 = 93
    GPA_7 = GPA_6 + 2
    GPA_8 = 91

    # Calculate the total GPA for all three grade levels
    total_GPA = GPA_6 + GPA_7 + GPA_8

    # Calculate the average GPA for the school
    average_GPA = total_GPA / 3

    # Display the average GPA for the school
    result = average_GPA
    return result

print(solution())