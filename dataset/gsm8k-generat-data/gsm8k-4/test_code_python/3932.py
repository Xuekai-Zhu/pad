def solution():
    """There is a lot of dust in Susie's house. It takes her 2 hours to vacuum the whole house. She can vacuum each room in 20 minutes. How many rooms does she have in her house?"""
    # Convert the total vacuuming time to minutes
    total_time = 2 * 60 

    # Calculate the time it takes to vacuum one room
    room_time = 20 

    # Calculate the number of rooms in the house
    rooms = total_time // room_time 

    result = rooms
    return result

print(solution())