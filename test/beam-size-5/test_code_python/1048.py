def solution():
    
    # Define the initial number of people on the train
    initial_people = 120

    # Calculate the number of people on the train at the first stop
    first_stop_people = initial_people + 20

    # Calculate the number of people on the train at the second stop
    second_stop_people = 50 + 2 * 50

    # Calculate the number of people on the train at the third station
    third_stop_people = 80

    # Calculate the total number of people on the train at the final stop
    final_people = initial_people + second_stop_people + third_stop_people

    # Display the total number of people on the train at the final stop
    result = final_people
    return result

print(solution())