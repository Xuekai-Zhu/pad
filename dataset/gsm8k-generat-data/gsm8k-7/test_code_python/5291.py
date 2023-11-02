def solution():
    initial_waiting_room = 22
    additional_people = 3
    total_waiting_room = initial_waiting_room + additional_people

    # Let's assume that there are "x" people in the interview room
    # According to the problem, 5 times the number of people in the interview room equals the total waiting room
    # So, 5x = total_waiting_room
    x = total_waiting_room / 5

    # Round "x" to the nearest whole number since we can't have fraction of people in the interview room
    num_people_in_interview_room = round(x)

    result = num_people_in_interview_room
    return result

print(solution())