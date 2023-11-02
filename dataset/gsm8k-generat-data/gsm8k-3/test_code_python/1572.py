def solution():
    """Barbara got a great deal on a new chest of drawers, but she has to take a lot of paper out of the drawers to be able to use it. She found 3 bundles of colored paper, 2 bunches of white paper, and 5 heaps of scrap paper. If a bunch holds 4 sheets of paper, a bundle holds 2 sheets of paper, and a heap holds 20 sheets of paper, how many sheets of paper did Barbara remove from the chest of drawers?"""
    # Define the number of sheets of paper in each type of bundle
    COLORED_SHEETS_PER_BUNDLE = 2
    WHITE_SHEETS_PER_BUNCH = 4
    SCRAP_SHEETS_PER_HEAP = 20

    # Define the number of each type of paper that Barbara found
    colored_bundles = 3
    white_bunches = 2
    scrap_heaps = 5

    # Calculate the total number of sheets of paper
    colored_sheets = colored_bundles * COLORED_SHEETS_PER_BUNDLE
    white_sheets = white_bunches * WHITE_SHEETS_PER_BUNCH
    scrap_sheets = scrap_heaps * SCRAP_SHEETS_PER_HEAP
    total_sheets = colored_sheets + white_sheets + scrap_sheets

    # Display the total number of sheets of paper removed
    result = total_sheets
    return result

print(solution())