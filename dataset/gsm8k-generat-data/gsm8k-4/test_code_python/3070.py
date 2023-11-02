def solution():
    """Brianna started out with a bag of 24 marbles. She lost four marbles through a hole in the bag. Then, she gave away twice as many marbles as she had lost through the hole in the bag. Finally, her dog ate half as many marbles as Brianna had lost through the hole in the bag. How many marbles did Brianna have remaining?"""
    # Define the initial number of marbles
    initial_marbles = 24

    # Subtract the marbles lost through the hole
    marbles_left = initial_marbles - 4

    # Calculate the number of marbles she gave away
    marbles_given_away = 2 * 4

    # Subtract the marbles given away
    marbles_left -= marbles_given_away

    # Calculate the number of marbles the dog ate
    marbles_eaten_by_dog = 4 / 2

    # Subtract the marbles eaten by the dog
    marbles_left -= marbles_eaten_by_dog

    result = marbles_left
    return result

print(solution())