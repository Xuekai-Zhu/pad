def solution():
    """Brianna started out with a bag of 24 marbles. She lost four marbles through a hole in the bag. Then, she gave away twice as many marbles as she had lost through the hole in the bag. Finally, her dog ate half as many marbles as Brianna had lost through the hole in the bag. How many marbles did Brianna have remaining?"""
    
    # Initialize the number of marbles Brianna started with
    marbles = 24

    # Remove the marbles lost through the hole
    marbles -= 4

    # Calculate the number of marbles given away
    given_away = 2 * 4

    # Remove the marbles given away
    marbles -= given_away

    # Calculate the number of marbles the dog ate
    eaten = 4 / 2

    # Remove the marbles eaten by the dog
    marbles -= eaten

    # Display the number of marbles Brianna has remaining
    result = marbles
    return result

print(solution())