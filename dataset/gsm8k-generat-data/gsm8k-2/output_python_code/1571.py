def solution():
    """Barbara got a great deal on a new chest of drawers, but she has to take a lot of paper out of the drawers to be able to use it. She found 3 bundles of colored paper, 2 bunches of white paper, and 5 heaps of scrap paper. If a bunch holds 4 sheets of paper, a bundle holds 2 sheets of paper, and a heap holds 20 sheets of paper, how many sheets of paper did Barbara remove from the chest of drawers?"""
    colored_paper = 3 * 2
    white_paper = 2 * 4
    scrap_paper = 5 * 20
    total_paper = colored_paper + white_paper + scrap_paper
    result = total_paper
    return result

print(solution())