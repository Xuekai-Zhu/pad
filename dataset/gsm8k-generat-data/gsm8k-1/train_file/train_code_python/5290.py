def solution():
    """There are twenty-two people in a waiting room. If three more people arrive, the number of people in the waiting room becomes five times the number of people inside the interview room. How many people are in the interview room?"""
    total_people = 22
    added_people = 3
    waiting_people = total_people + added_people
    interview_people = waiting_people / 5
    result = interview_people
    return result

print(solution())