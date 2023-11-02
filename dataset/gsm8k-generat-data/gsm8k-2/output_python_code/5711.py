def solution():
    """An airline company owns 5 airplanes. Every airplane they own has 20 rows with 7 seats in each row. Each airplane makes 2 flights a day. How many passengers can the airline company accommodate each day?"""
    num_airplanes = 5
    num_rows = 20
    num_seats_per_row = 7
    num_flights_per_day = 2

    num_passengers_per_plane = num_rows * num_seats_per_row
    num_passengers_per_flight = num_passengers_per_plane * num_airplanes
    num_passengers_per_day = num_passengers_per_flight * num_flights_per_day

    result = num_passengers_per_day
    return result

print(solution())