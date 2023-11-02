def solution():
    """Pete has a bag with 10 marbles. 40% are blue and the rest are red. His friend will trade him two blue marbles for every red one. If Pete keeps 1 red marble, how many total marbles does he have after trading with his friend?"""
    # Define the initial number of marbles
    initial_marbles = 10

    # Calculate the number of blue marbles
    blue_marbles = initial_marbles * 0.4

    # Calculate the number of red marbles
    red_marbles = initial_marbles - blue_marbles

    # Keep one red marble
    red_marbles -= 1

    # Trade two blue marbles for one red marble
    traded_blue_marbles = red_marbles * 2
    blue_marbles -= traded_blue_marbles

    # Calculate the total number of marbles
    total_marbles = blue_marbles + red_marbles + 1

    result = total_marbles
    return result

print(solution())