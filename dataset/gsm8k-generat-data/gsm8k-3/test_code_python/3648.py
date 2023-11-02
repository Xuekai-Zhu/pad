def solution():
    """Carla is dividing up chores for her two kids, Anna and Billy. She wants each of them to spend the same number of minutes working. Sweeping takes 3 minutes per room, washing the dishes takes 2 minutes per dish, and doing laundry takes 9 minutes per load. If Anna does the sweeping for 10 rooms and Billy does two loads of laundry, how many dishes should Billy wash so they spend the same amount of time doing chores?"""
    # Define the time it takes to do each chore
    SWEEP_TIME = 3
    DISH_TIME = 2
    LAUNDRY_TIME = 9

    # Define the number of rooms and loads for Anna and Billy
    anna_rooms = 10
    billy_loads = 2

    # Calculate the total time Anna and Billy spend on chores
    anna_time = anna_rooms * SWEEP_TIME
    billy_time = billy_loads * LAUNDRY_TIME

    # Calculate the number of dishes Billy should wash to spend the same amount of time as Anna
    dishes = (anna_time - billy_time) / DISH_TIME

    # Display the number of dishes Billy should wash
    result = dishes
    return result

print(solution())