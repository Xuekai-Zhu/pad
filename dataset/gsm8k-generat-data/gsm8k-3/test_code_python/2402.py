def solution():
    """One-third of a class of 39 students took part in a math competition. How many students did not participate in the competition?"""
    # Calculate the number of students who participated in the competition
    participants = 39 // 3

    # Calculate the number of students who did not participate
    non_participants = 39 - participants

    # Display the number of students who did not participate
    result = non_participants
    return result

print(solution())