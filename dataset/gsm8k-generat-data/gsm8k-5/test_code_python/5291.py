def solution():
    initial_waiting_room = 22  # There are initially 22 people in the waiting room
    extra_people = 3  # 3 more people arrive

    # Calculate the total number of people in the waiting room after the extra people arrive
    total_waiting_room = initial_waiting_room + extra_people

    # Let x be the number of people in the interview room
    # From the problem description: total_waiting_room = 5*x
    x = total_waiting_room / 5

    # Round x to the nearest whole number since you can't have a fraction of a person
    interview_room = round(x)
    result = interview_room
    return result

print(solution())