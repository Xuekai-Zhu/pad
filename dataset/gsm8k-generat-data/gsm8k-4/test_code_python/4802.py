def solution():
    """The battery charge in Mary’s cordless vacuum cleaner lasts ten minutes. It takes her four minutes to vacuum each room in her house. Mary has three bedrooms, a kitchen, and a living room. How many times does Mary need to charge her vacuum cleaner to vacuum her whole house?"""
    # Define the battery charge time and the time to vacuum each room
    BATTERY_TIME = 10
    ROOM_TIME = 4

    # Define the number of rooms in Mary's house
    NUM_ROOMS = 5

    # Calculate the total time needed to vacuum the entire house
    total_time = NUM_ROOMS * ROOM_TIME

    # Calculate the number of times Mary needs to charge her vacuum cleaner
    num_charges = total_time // BATTERY_TIME + 1

    # return the result
    result = num_charges
    return result

print(solution())