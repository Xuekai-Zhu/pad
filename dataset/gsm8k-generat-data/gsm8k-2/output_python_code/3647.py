def solution():
    """Carla is dividing up chores for her two kids, Anna and Billy. She wants each of them to spend the same number of minutes working. Sweeping takes 3 minutes per room, washing the dishes takes 2 minutes per dish, and doing laundry takes 9 minutes per load. If Anna does the sweeping for 10 rooms and Billy does two loads of laundry, how many dishes should Billy wash so they spend the same amount of time doing chores?"""
    anna_sweeping_time = 10 * 3
    billy_laundry_time = 2 * 9
    total_time = anna_sweeping_time + billy_laundry_time
    dishes_to_wash = total_time / 2 - anna_sweeping_time
    result = dishes_to_wash
    return result

print(solution())