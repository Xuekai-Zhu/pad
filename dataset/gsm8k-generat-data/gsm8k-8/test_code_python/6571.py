def solution():
    # Define initial number of marbles for Sam and Steve
    sams_marbles = 2 * steves_marbles
    sallys_marbles = sams_marbles - 5

    # Calculate how many marbles Sam gives away
    num_given_away = 3 * 2

    # Calculate new number of marbles for Sam and Sally
    sams_marbles = sams_marbles - num_given_away
    sallys_marbles = sallys_marbles + num_given_away

    # Calculate new number of marbles for Steve
    steves_marbles = (8 + num_given_away - sallys_marbles) / 2

    result = steves_marbles
    return result

print(solution())