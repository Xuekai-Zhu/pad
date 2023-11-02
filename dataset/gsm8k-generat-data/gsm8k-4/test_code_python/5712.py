def solution():
    """An airline company owns 5 airplanes. Every airplane they own has 20 rows with 7 seats in each row. Each airplane makes 2 flights a day. How many passengers can the airline company accommodate each day?"""
    # Define the number of airplanes and the number of rows and seats per airplane
    airplanes = 5
    rows = 20
    seats = 7

    # Calculate the total number of seats per airplane
    total_seats = rows * seats

    # Calculate the total number of passengers per airplane per flight
    passengers_per_flight = total_seats

    # Calculate the total number of passengers per airplane per day
    passengers_per_day = passengers_per_flight * 2

    # Calculate the total number of passengers the airline company can accommodate per day
    total_passengers = passengers_per_day * airplanes

    # return the result
    result = total_passengers
    return result

print(solution())