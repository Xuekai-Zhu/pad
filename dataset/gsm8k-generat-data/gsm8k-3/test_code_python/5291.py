def solution():
    """There are twenty-two people in a waiting room. If three more people arrive, the number of people in the waiting room becomes five times the number of people inside the interview room. How many people are in the interview room?"""
    # Define the number of people in the waiting room and the number of people who arrived
    waiting_room = 22
    arrived_people = 3

    # Calculate the total number of people after the new arrivals
    total_people = waiting_room + arrived_people

    # Calculate the number of people in the interview room
    interview_room = total_people / 5

    # Display the number of people in the interview room
    result = interview_room
    return result

print(solution())