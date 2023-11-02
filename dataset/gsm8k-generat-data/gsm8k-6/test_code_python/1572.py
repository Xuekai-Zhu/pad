def solution():
    # Calculate the total number of sheets of paper removed from the chest of drawers
    colored_paper = 3 * 2  # 3 bundles of colored paper, with 2 sheets in each bundle
    white_paper = 2 * 4  # 2 bunches of white paper, with 4 sheets in each bunch
    scrap_paper = 5 * 20  # 5 heaps of scrap paper, with 20 sheets in each heap
    total_paper = colored_paper + white_paper + scrap_paper
    result = total_paper
    return result

print(solution())