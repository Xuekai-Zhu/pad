def solution():
    # Define the initial number of people on the bus
    num_people = 50

    # Subtract the number of people who got off at the first stop
    num_people -= 15

    # Subtract the number of people who got off and add the number who got on at the second stop
    num_people -= 8
    num_people += 2

    # Subtract the number of people who got off and add the number who got on at the third stop
    num_people -= 4
    num_people += 3

    result = num_people
    return result

print(solution())