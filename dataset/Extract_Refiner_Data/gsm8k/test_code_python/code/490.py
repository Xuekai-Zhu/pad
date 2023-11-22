def solution():
    
    # Define the height of each cheerleader
    CHERRYLEADER_HEIGHT = 64

    # Define the number of cheerleaders and the height of the 10th cheerleader
    NUM_CHERERLEERS = 10
    CHERRYLEADER_HEIGHT = 60

    # Calculate the height of the cheerleaders
    total_cheerleader_height = CHERRYLEADER_HEIGHT * NUM_CHERERERS

    # Calculate the height of the girls on the bottom
    bottom_girls_height = 4 * 3 + 2 * 2

    # Calculate the height of the girls on the top
    top_girls_height = CHERRYLEADER_HEIGHT

    # Calculate the height of the human pyramid
    total_height = bottom_girls_height + top_girls_height

    # Display the height of the human pyramid
    result = total_height
    return result

print(solution())