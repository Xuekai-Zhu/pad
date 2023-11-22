def solution():
    
    # Define the initial number of passengers
    passengers = 48

    # Calculate the number of passengers who got off on the first stop
    passengers -= 8

    # Calculate the number of passengers who got off on the second stop
    passengers -= 8

    # Calculate the number of passengers who got off on the second stop
    passengers -= 5 * 8

    # Calculate the number of passengers who got off on the second stop
    passengers -= 3 * 21

    # Calculate the total number of passengers after the second stop
    total_passengers = passengers

    # Display the total number of passengers
    result = total_passengers
    return result

print(solution())