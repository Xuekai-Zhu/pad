def solution():
    """There is a lot of dust in Susie's house. It takes her 2 hours to vacuum the whole house. She can vacuum each room in 20 minutes. How many rooms does she have in her house?"""
    total_time = 2 * 60
    room_time = 20
    num_rooms = total_time // room_time
    result = num_rooms
    return result

print(solution())