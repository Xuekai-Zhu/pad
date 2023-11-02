def solution():
    """Once a week, it takes Kitty 5 minutes to pick up toys and straighten the living room. It takes another 20 minutes to vacuum the living room floor, seating and drapes. She spends 15 minutes cleaning the windows and 10 minutes dusting the furniture. After 4 weeks, how long has Kitty spent cleaning just the living room?"""
    time_pickup = 5
    time_vacuum = 20
    time_windows = 15
    time_dusting = 10
    total_cleaning_time = (time_pickup + time_vacuum + time_windows + time_dusting) * 4
    result = total_cleaning_time
    return result

print(solution())