def solution():
    """Ms. Mitsuko told the class that if the average score on their quiz is higher than 75% then they will get a pizza party. There are 25 students in the class. One student is absent and has to take the test the next day. The average score of the students who took the test was 77%. What is the lowest grade the absent student can get for the class to still get a pizza party?"""
    # Calculate the total possible points on the quiz
    total_points = 25 * 100

    # Calculate the total points earned by the students who took the quiz
    total_points_earned = 24 * 77

    # Calculate the minimum points the absent student must earn
    min_points = 0.75 * total_points - total_points_earned

    # Convert the minimum points to a percentage grade
    min_grade = min_points / 100

    # Display the minimum grade the absent student must earn
    result = min_grade
    return result

print(solution())