def solution():
    
    # Define the initial number of people on the train
    initial_people = 172

    # Calculate the number of people on the first stop
    first_stop_people = initial_people - 47

    # Calculate the number of people on the second stop
    second_stop_people = initial_people + 13

    # Calculate the total number of people on the train
    total_people = initial_people + second_stop_people

    # Display the total number of people on the train
    result = total_people
    return result

print(solution())