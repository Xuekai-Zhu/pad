def solution():
    """Carla is dividing up chores for her two kids, Anna and Billy. She wants each of them to spend the same number of minutes working.
    Sweeping takes 3 minutes per room, washing the dishes takes 2 minutes per dish, and doing laundry takes 9 minutes per load. 
    If Anna does the sweeping for 10 rooms and Billy does two loads of laundry, how many dishes should Billy wash so they spend the same amount of time doing chores?"""
    anna_sweep_time = 3 * 10
    billy_laundry_time = 9 * 2
    total_chore_time = anna_sweep_time + billy_laundry_time
    dishes_time_each = total_chore_time / 2 - billy_laundry_time
    dishes_to_wash = dishes_time_each / 2
    result = dishes_to_wash
    return result

print(solution())