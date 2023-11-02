def solution():
    airplanes = 5  # The airline company owns 5 airplanes
    rows = 20  # Each airplane has 20 rows
    seats_in_each_row = 7  # Each row has 7 seats
    flights_per_day = 2  # Each airplane makes 2 flights a day

    # Calculate the total number of seats in each airplane
    total_seats_per_airplane = rows * seats_in_each_row

    # Calculate the total number of passengers each airplane can accommodate in a day
    passengers_per_airplane = total_seats_per_airplane * flights_per_day

    # Calculate the total number of passengers the airline company can accommodate each day
    total_passengers = passengers_per_airplane * airplanes
    result = total_passengers
    return result

print(solution())