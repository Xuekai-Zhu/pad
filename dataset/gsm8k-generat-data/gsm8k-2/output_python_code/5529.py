def solution():
    """Simon is picking blueberries to make blueberry pies. He picks 100 blueberries from his own bushes and another 200 blueberries from blueberry bushes growing nearby. If each pie needs 100 blueberries, how many blueberry pies can Simon make?"""
    total_blueberries = 100 + 200
    blueberries_per_pie = 100
    pies = total_blueberries // blueberries_per_pie
    result = pies
    return result

print(solution())