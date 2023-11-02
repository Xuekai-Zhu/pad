def solution():
    # Start with 40 marbles
    total_marbles = 40

    # Subtract 3 marbles from playing at breakfast
    total_marbles -= 3

    # Give 5 marbles to Susie at lunchtime
    total_marbles -= 5

    # Add 12 marbles from mom in the afternoon
    total_marbles += 12

    # Receive twice as many marbles as given from Susie
    total_marbles += 2 * 5

    result = total_marbles
    return result

print(solution())