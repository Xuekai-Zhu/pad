def solution():
    """The math teacher would be happy if the class average test score was at least 85. There are 10 students in the class, 5 of which scored a 92 on the test and 4 of which scored an 80. What would the last student have to score to at least make the teacher happy?"""
    # Define the total number of students and the desired average score
    num_students = 10
    desired_avg = 85

    # Define the number of students who scored a 92 and their total score
    num_high_scores = 5
    total_high_score = num_high_scores * 92

    # Define the number of students who scored an 80 and their total score
    num_low_scores = 4
    total_low_score = num_low_scores * 80

    # Calculate the minimum score the last student needs to achieve the desired average
    min_last_score = (desired_avg * num_students) - (total_high_score + total_low_score)

    # Return the result
    result = min_last_score
    return result

print(solution())