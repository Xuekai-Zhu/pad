def solution():
    """Once a week, it takes Kitty 5 minutes to pick up toys and straighten the living room. It takes another 20 minutes to vacuum the living room floor, seating and drapes. She spends 15 minutes cleaning the windows and 10 minutes dusting the furniture. After 4 weeks, how long has Kitty spent cleaning just the living room?"""
    pick_up_time = 5
    vacuum_time = 20
    window_cleaning_time = 15
    dusting_time = 10
    total_time = pick_up_time + vacuum_time + window_cleaning_time + dusting_time
    weeks = 4
    total_time *= weeks
    result = total_time
    return result

print(solution())