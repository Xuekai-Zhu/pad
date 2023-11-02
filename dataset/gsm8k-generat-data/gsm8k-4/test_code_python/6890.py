def solution():
    """Christopher, Jameson, and June each bought a toy sword. June's sword is 5 inches longer than Jameson's sword. Jameson's sword is 3 inches longer than twice the length of Christopher's sword. Christopher's sword is 15 inches long. How many inches longer is June's sword than Christopher's sword?"""
    # Define the length of Christopher's sword
    chris_sword = 15

    # Calculate the length of Jameson's sword
    jameson_sword = 2 * chris_sword + 3

    # Calculate the length of June's sword
    june_sword = jameson_sword + 5

    # Calculate the difference between June's sword and Christopher's sword
    difference = june_sword - chris_sword

    result = difference
    return result

print(solution())