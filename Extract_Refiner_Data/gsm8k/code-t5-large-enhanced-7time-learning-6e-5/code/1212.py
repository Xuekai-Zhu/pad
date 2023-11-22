def solution():
    
    # Define the capacity of the bus and the number of people on the first stop
    BUS_CAPACITY = 200
    FIRST_STOP_CAPACITY = 20

    # Calculate the number of people who entered the bus at the first station
    first_station_passengers = 40

    # Calculate the number of passengers who entered the bus at the second station
    second_station_passengers = first_station_passengers * (3/4)

    # Calculate the number of passengers on the bus at the second station
    second_station_passengers = first_station_passengers + second_station_passengers

    # Calculate the number of passengers on the bus at the third station
    third_station_passengers = second_station_passengers * 2

    # Calculate the total number of passengers on the bus
    total_passengers = FIRST_STOP_CAPACITY + second_station_passengers + third_station_passengers

    # Display the total number of passengers required to fill the remaining

print(solution())