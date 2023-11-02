def solution():
    """Once a week, it takes Kitty 5 minutes to pick up toys and straighten the living room. It takes another 20 minutes to vacuum the living room floor, seating and drapes. She spends 15 minutes cleaning the windows and 10 minutes dusting the furniture. After 4 weeks, how long has Kitty spent cleaning just the living room?"""
    # Define the time it takes to clean each area of the living room
    pickup_time = 5
    vacuum_time = 20
    window_time = 15
    dusting_time = 10

    # Calculate the total cleaning time for one week
    weekly_time = pickup_time + vacuum_time + window_time + dusting_time

    # Calculate the total cleaning time for 4 weeks
    total_time = weekly_time * 4

    # return the result
    result = total_time
    return result

print(solution())