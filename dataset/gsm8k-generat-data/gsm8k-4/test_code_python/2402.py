def solution():
    """One-third of a class of 39 students took part in a math competition. How many students did not participate in the competition?"""
    # Calculate the number of students who took part in the competition
    competition_students = 39 // 3

    # Calculate the number of students who did not participate in the competition
    non_competition_students = 39 - competition_students

    # return the result
    result = non_competition_students
    return result

print(solution())