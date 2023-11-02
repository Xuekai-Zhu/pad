def solution():
    """Tom is cutting a piece of wood to make a shelf. He cut the wood to 143 cm, but it is too long to fit in the bookshelf he is making. He decides to cut 25 cm off the board. But it turned out longer than the other boards. He had to cut off 7 cm from each to make them the same size. How long were the boards before he cut the 7 cm off?"""
    # Define the length of the original board
    original_length = None

    # Calculate the length of the board after cutting off 25 cm
    length_after_cutting = 143 - 25

    # Calculate the length of the other two boards after cutting off 7 cm
    length_after_cutting_other_boards = length_after_cutting - 7

    # Calculate the original length of all three boards before cutting off 7 cm
    original_length_all_boards = (length_after_cutting_other_boards + 7) * 3

    # Calculate the original length of the board in question
    original_length = original_length_all_boards - length_after_cutting

    result = original_length
    return result

print(solution())