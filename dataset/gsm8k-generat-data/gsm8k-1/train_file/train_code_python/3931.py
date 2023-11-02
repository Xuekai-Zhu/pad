def solution():
    """There is a lot of dust in Susie's house. It takes her 2 hours to vacuum the whole house. She can vacuum each room in 20 minutes. How many rooms does she have in her house?"""
    total_time = 2 # in hours
    time_per_room = 20/60 # in hours
    total_rooms = total_time / time_per_room
    result = total_rooms
    return result

print(solution())