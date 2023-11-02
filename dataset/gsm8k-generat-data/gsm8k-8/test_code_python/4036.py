def solution():
    # Initialize variables
    cakes_on_sixth_day = 320
    cakes_on_first_day = 1

    # Loop through the days, calculating the number of cakes made each day
    for day in range(2, 7):
        cakes_on_first_day *= 2

    # Calculate the number of cakes made on the first day
    cakes_on_first_day = cakes_on_sixth_day / (cakes_on_first_day + 2)

    result = cakes_on_first_day
    return result

print(solution())