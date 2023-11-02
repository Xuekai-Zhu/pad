def solution():
    # Calculate the total number of colored paper sheets
    colored_paper = 3 * 2  # 3 bundles of colored paper, each with 2 sheets

    # Calculate the total number of white paper sheets
    white_paper = 2 * 4  # 2 bunches of white paper, each with 4 sheets

    # Calculate the total number of scrap paper sheets
    scrap_paper = 5 * 20  # 5 heaps of scrap paper, each with 20 sheets

    # Calculate the total number of paper sheets removed from the chest of drawers
    total_paper = colored_paper + white_paper + scrap_paper
    result = total_paper
    return result

print(solution())