def solution():
    """Carla is dividing up chores for her two kids, Anna and Billy. She wants each of them to spend the same number of minutes working. Sweeping takes 3 minutes per room, washing the dishes takes 2 minutes per dish, and doing laundry takes 9 minutes per load. If Anna does the sweeping for 10 rooms and Billy does two loads of laundry, how many dishes should Billy wash so they spend the same amount of time doing chores?"""
    # Define the time it takes to do each chore
    sweeping_time = 3
    dishes_time = 2
    laundry_time = 9

    # Define the number of rooms to sweep and loads of laundry to do
    num_rooms = 10
    num_laundry = 2

    # Calculate the total time Anna spends working
    anna_time = num_rooms * sweeping_time

    # Calculate the total time Billy spends working
    billy_time = num_laundry * laundry_time

    # Calculate the number of dishes Billy needs to wash to spend the same amount of time as Anna
    num_dishes = (anna_time - billy_time) / dishes_time

    # return the result
    result = num_dishes
    return result

print(solution())