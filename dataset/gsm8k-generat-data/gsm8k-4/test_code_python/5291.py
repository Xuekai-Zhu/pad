def solution():
    """There are twenty-two people in a waiting room. If three more people arrive, the number of people in the waiting room becomes five times the number of people inside the interview room. How many people are in the interview room?"""
    # Define the initial number of people in the waiting room
    waiting_room = 22

    # Define the number of people who arrive
    arrive = 3

    # Define the total number of people after the arrival
    total_people = waiting_room + arrive

    # Define the number of people in the interview room
    interview_room = total_people / 5

    # Return the result
    result = interview_room
    return result

print(solution())