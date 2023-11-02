def solution():
    """Christopher, Jameson, and June each bought a toy sword. June's sword is 5 inches longer than Jameson's sword. Jameson's sword is 3 inches longer than twice the length of Christopher's sword. Christopher's sword is 15 inches long. How many inches longer is June's sword than Christopher's sword?"""
    christopher_sword = 15
    jameson_sword = 2 * christopher_sword + 3
    june_sword = jameson_sword + 5
    difference = june_sword - christopher_sword
    result = difference
    return result

print(solution())