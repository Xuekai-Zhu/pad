def solution():
    # Calculate the total time spent by Anna and Billy on sweeping and laundry
    anna_time = 10 * 3  # Anna spends 3 minutes per room sweeping 10 rooms
    billy_time = 2 * 9  # Billy spends 9 minutes per load of laundry for 2 loads

    # Calculate the total number of dishes Billy needs to wash
    dishes = (anna_time - billy_time) / 2  # Billy needs to spend the same amount of time as Anna
    result = dishes
    return result

print(solution())