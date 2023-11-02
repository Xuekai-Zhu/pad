def solution():
    """There are twenty-two people in a waiting room. If three more people arrive, the number of people in the waiting room becomes five times the number of people inside the interview room. How many people are in the interview room?"""
    waiting_room = 22
    added_people = 3
    waiting_total = waiting_room + added_people
    interview_total = waiting_total / 5
    result = interview_total
    return result

print(solution())