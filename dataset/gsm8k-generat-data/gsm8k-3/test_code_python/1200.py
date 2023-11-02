def solution():
    """Once a week, it takes Kitty 5 minutes to pick up toys and straighten the living room.  It takes another 20 minutes to vacuum the living room floor, seating and drapes.  She spends 15 minutes cleaning the windows and 10 minutes dusting the furniture.  After 4 weeks, how long has Kitty spent cleaning just the living room?"""
    # Define the time it takes to complete each cleaning task
    PICKUP_TIME = 5
    VACUUM_TIME = 20
    WINDOW_TIME = 15
    DUST_TIME = 10

    # Calculate the total time spent cleaning the living room over 4 weeks
    total_time = 4 * (PICKUP_TIME + VACUUM_TIME + WINDOW_TIME + DUST_TIME)

    # Display the total time spent cleaning the living room
    result = total_time
    return result

print(solution())