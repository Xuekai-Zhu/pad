def solution():
    # Calculate the total number of seats
    total_seats = 15 * 10

    # Calculate the number of usualy unseated seats
    unseated_seats = total_seats / 10

    # Calculate the number of usually seated seats
    seated_seats = total_seats - unseated_seats
    
    result = seated_seats
    return result

print(solution())