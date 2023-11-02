def solution():
    # Define the initial number of people in the waiting room and the number of people who arrived
    waiting_room = 22
    arrived = 3

    # Calculate the total number of people after the arrival
    total = waiting_room + arrived

    # Calculate the number of people in the interview room
    interview_room = total / 5

    result = interview_room
    return result

print(solution())