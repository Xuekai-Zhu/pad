def solution():
    """Barbara got a great deal on a new chest of drawers, but she has to take a lot of paper out of the drawers to be able to use it. She found 3 bundles of colored paper, 2 bunches of white paper, and 5 heaps of scrap paper. If a bunch holds 4 sheets of paper, a bundle holds 2 sheets of paper, and a heap holds 20 sheets of paper, how many sheets of paper did Barbara remove from the chest of drawers?"""
    # Define the number of sheets of paper in each type of paper
    colored_sheets = 3 * 2
    white_sheets = 2 * 4
    scrap_sheets = 5 * 20

    # Calculate the total number of sheets of paper removed
    total_sheets = colored_sheets + white_sheets + scrap_sheets

    # return the result
    result = total_sheets
    return result

print(solution())