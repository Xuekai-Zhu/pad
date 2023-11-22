def solution():
    
    # Define the initial number of people
    initial_people = 172

    # Subtract the number of people who got off at the first stop
    people_after_first_stop = initial_people - 47

    # Add the number of people who got on at the second stop
    people_after_second_stop = people_after_first_stop + 13 - 38

    # Display the number of people on the train
    result = people_after_second_stop
    return result

print(solution())