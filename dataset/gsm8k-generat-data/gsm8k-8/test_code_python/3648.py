def solution():
    # Calculate the total time Anna spends on sweeping
    anna_sweeping_time = 3 * 10

    # Calculate the total time Billy spends on laundry
    billy_laundry_time = 2 * 9 * 2

    # Calculate the total time Anna and Billy spend on chores
    total_time = anna_sweeping_time + billy_laundry_time

    # Calculate the number of dishes Billy needs to wash to spend the same amount of time as Anna
    billy_dish_time = total_time / 2 - billy_laundry_time
    dishes_to_wash = billy_dish_time / 2

    result = dishes_to_wash
    return result

print(solution())