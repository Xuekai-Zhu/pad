def solution():
    """My brother and I have thirty minutes to go to school, without being late. It takes us 15 minutes to arrive at the school gate,
    and another 6 minutes to get to the school building. How much time do we have to get to our room, without being late?"""
    
    # Define the time it takes to get from the school gate to the school building
    SCHOOL_BUILDING_TIME = 6

    # Define the total time we have to get to our room
    TOTAL_TIME = 30

    # Calculate the time it takes to get from our arrival point to our room
    room_time = TOTAL_TIME - (15 + SCHOOL_BUILDING_TIME)

    # Return the result
    result = room_time
    return result

print(solution())