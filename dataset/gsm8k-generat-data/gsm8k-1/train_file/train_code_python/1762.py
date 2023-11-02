def solution():
    """ My brother and I have thirty minutes to go to school, without being late. It takes us 15 minutes to arrive at the school gate, and another 6 minutes to get to the school building. How much time do we have to get to our room, without being late?"""
    total_time = 30
    arrival_time = 15
    building_time = 6
    room_time = total_time - arrival_time - building_time
    result = room_time
    return result

print(solution())