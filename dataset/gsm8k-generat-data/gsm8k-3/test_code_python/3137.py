def solution():
    """The math teacher would be happy if the class average test score was at least 85. There are 10 students in the class, 5 of which scored a 92 on the test and 4 of which scored an 80. What would the last student have to score to at least make the teacher happy?"""
    # Determine the total score of the first 9 students
    total_score = 5 * 92 + 4 * 80

    # Determine the minimum score required for the 10th student to raise the class average to at least 85
    min_score = (85 * 10) - total_score

    # Display the minimum score required for the 10th student
    result = min_score
    return result

print(solution())