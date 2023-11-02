def solution():
    """An airline company owns 5 airplanes. Every airplane they own has 20 rows with 7 seats in each row. Each airplane makes 2 flights a day. How many passengers can the airline company accommodate each day?"""
    airplanes_owned = 5
    rows_per_airplane = 20
    seats_per_row = 7
    flights_per_day = 2
    passengers_per_flight = rows_per_airplane * seats_per_row
    total_passengers_per_day = airplanes_owned * flights_per_day * passengers_per_flight
    result = total_passengers_per_day
    return result

print(solution())