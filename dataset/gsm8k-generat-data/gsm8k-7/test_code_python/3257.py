def solution():
    initial_passengers = 50
    passengers_at_first_stop = initial_passengers + 16

    # Calculate the number of passengers at each of the following stops
    passengers_at_second_stop = passengers_at_first_stop - 22
    passengers_at_third_stop = passengers_at_second_stop - 22
    passengers_at_fourth_stop = passengers_at_third_stop - 22
    passengers_at_last_stop = passengers_at_fourth_stop + 5

    result = passengers_at_last_stop
    return result

print(solution())