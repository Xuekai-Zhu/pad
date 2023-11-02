def solution():
    # Define the length of Christopher's sword
    christopher_sword = 15

    # Calculate the length of Jameson's sword
    jameson_sword = 3 + 2 * christopher_sword

    # Calculate the length of June's sword
    june_sword = jameson_sword + 5

    # Calculate the difference in length between June's and Christopher's swords
    difference = june_sword - christopher_sword
    result = difference
    return result

print(solution())