def solution():
    """Pete has a bag with 10 marbles. 40% are blue and the rest are red. His friend will trade him two blue marbles for every red one. If Pete keeps 1 red marble, how many total marbles does he have after trading with his friend?"""
    # Define the number of marbles Pete has
    NUM_MARBLES = 10
    # Calculate the number of blue marbles
    blue_marbles = round(NUM_MARBLES * 0.4)
    # Calculate the number of red marbles
    red_marbles = NUM_MARBLES - blue_marbles
    # Trade 2 blue marbles for every red marble (except one)
    traded_blue = (red_marbles - 1) * 2
    # Calculate the new number of blue marbles
    new_blue = blue_marbles + traded_blue
    # Calculate the new number of red marbles
    new_red = 1
    # Calculate the total number of marbles
    total_marbles = new_blue + new_red
    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())