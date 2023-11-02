def solution():
    # Calculate the total number of seats on the bus
    total_seats = 23 * 4

    # Calculate the number of people on the bus after the first stop
    first_stop_people = 16 + 15 - 3

    # Calculate the number of people on the bus after the second stop
    second_stop_people = first_stop_people + 17 - 10

    # Calculate the number of empty seats on the bus after the second stop
    empty_seats = total_seats - second_stop_people
    result = empty_seats
    return result

print(solution())