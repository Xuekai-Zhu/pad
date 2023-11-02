def solution():
    """Tom is cutting a piece of wood to make a shelf. He cut the wood to 143 cm, but it is too long to fit in the bookshelf he is making. He decides to cut 25 cm off the board. But it turned out longer than the other boards. He had to cut off 7 cm from each to make them the same size. How long were the boards before he cut the 7 cm off?"""
    initial_length = 143
    length_after_first_cut = initial_length - 25
    final_length = length_after_first_cut - 7
    initial_length_of_other_boards = final_length + 7
    result = initial_length_of_other_boards
    return result

print(solution())