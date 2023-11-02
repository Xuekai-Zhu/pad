def solution():
    """My brother and I have thirty minutes to go to school, without being late. It takes us 15 minutes to arrive at the school gate, and another 6 minutes to get to the school building. How much time do we have to get to our room, without being late?"""
    # Define the total time available without being late
    TOTAL_TIME = 30

    # Define the time it takes to get to the school gate and building
    GATE_TIME = 15
    BUILDING_TIME = 6

    # Calculate the time remaining to get to our room
    remaining_time = TOTAL_TIME - (GATE_TIME + BUILDING_TIME)

    # Display the time remaining
    result = remaining_time
    return result

print(solution())