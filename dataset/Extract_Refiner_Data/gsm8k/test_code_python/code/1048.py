def solution():
    
    # Define the initial number of people on the train
    initial_people = 120

    # Calculate the number of people boarding at the first stop
    first_stop_people = initial_people + 20

    # Calculate the number of people descending at the second stop
    second_stop_people = 50 * 2

    # Calculate the number of people descending at the third station
    third_station_people = 80

    # Calculate the total number of people on the train at the final stop
    final_stop_people = initial_people + first_stop_people + second_stop_people + third_station_people

    # Display the total number of people on the train at the final stop
    result = final_stop_people
    return result

print(solution())