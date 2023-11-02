def solution():
    """Lana is brewing cups of tea for her friends. She has 27 cups, and she divides these into 3 rows. In each row, she creates equal amounts of chamomile and mint tea cups. She then uses the remaining cups to brew a total of 15 cups of cinnamon tea. How many cups of mint tea are in each row?"""
    total_cups = 27
    rows = 3
    cinnamon_cups = 15
    chamomile_cups = total_cups - cinnamon_cups

    mint_cups_per_row = chamomile_cups // (2 * rows)

    result = mint_cups_per_row
    return result

print(solution())