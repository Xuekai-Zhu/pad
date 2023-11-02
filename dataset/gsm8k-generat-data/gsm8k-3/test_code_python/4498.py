def solution():
    """Tom is cutting a piece of wood to make a shelf. He cut the wood to 143 cm, but it is too long to fit in the bookshelf he is making. He decides to cut 25 cm off the board. But it turned out longer than the other boards. He had to cut off 7 cm from each to make them the same size. How long were the boards before he cut the 7 cm off?"""
    # Define the original length of the board
    original_length = 0

    # Calculate the original length of the board
    # Start by adding the length of the board before Tom cut 25 cm off
    original_length += 143 + 25

    # Then, subtract the 7 cm that Tom had to cut off each of the other boards
    original_length -= 7 * 2

    # Display the original length of the board
    result = original_length
    return result

print(solution())