def solution():
    """A total of 107 oranges are picked by Del and Juan. Del picked 23 on each of 2 days and Juan picked the rest. How many oranges did Juan pick?"""
    # Define the number of oranges Del picked on each of the 2 days
    del_oranges_each_day = 23

    # Calculate the total number of oranges Del picked
    del_total_oranges = del_oranges_each_day * 2

    # Calculate the number of oranges Juan picked
    juan_oranges = 107 - del_total_oranges

    # Display the number of oranges Juan picked
    result = juan_oranges
    return result

print(solution())