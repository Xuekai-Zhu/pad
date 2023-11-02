def solution():
    """An airline company owns 5 airplanes. Every airplane they own has 20 rows with 7 seats in each row. Each airplane makes 2 flights a day. How many passengers can the airline company accommodate each day?"""
    # Define the number of airplanes, rows per airplane, seats per row, and flights per day
    airplanes = 5
    rows = 20
    seats = 7
    flights_per_day = 2

    # Calculate the total number of seats per airplane and the total number of seats for all airplanes
    seats_per_airplane = rows * seats
    total_seats = airplanes * seats_per_airplane

    # Calculate the total number of passengers per flight and per day
    total_passengers_per_flight = seats_per_airplane
    total_passengers_per_day = total_passengers_per_flight * flights_per_day * airplanes

    # Display the total number of passengers the airline can accommodate each day
    result = total_passengers_per_day
    return result

print(solution())