def solution():
    # Calculate the number of people who entered the bus at the first stop
    first_stop = 40

    # Calculate the number of people who entered the bus at the second station
    second_station = (3/4) * first_stop

    # Calculate the number of people who entered the bus at the third station
    third_station = (2/4) * first_stop

    # Calculate the total number of people who entered the bus
    total_passengers = first_stop + second_station + third_station

    # Calculate the number of people required to fill the remaining spaces
    remaining_people = 200 - total_passengers
    result = remaining_people
    return result

print(solution())