def solution():
    """One-third of a class of 39 students took part in a math competition. How many students did not participate in the competition?"""
    total_students = 39
    competition_participants = total_students / 3
    non_participants = total_students - competition_participants
    result = non_participants
    return result

print(solution())