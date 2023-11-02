def solution():
    # Calculate the number of seats in each airplane
    seats_per_airplane = 20 * 7

    # Calculate the number of passengers each airplane can accommodate per day
    passengers_per_airplane_per_day = seats_per_airplane * 2

    # Calculate the total number of passengers the airline company can accommodate each day
    total_passengers_per_day = passengers_per_airplane_per_day * 5
    result = total_passengers_per_day
    return result

print(solution())