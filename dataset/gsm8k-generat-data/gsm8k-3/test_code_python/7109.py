def solution():
    """Michelle had some leftover cans of silly string from her birthday party. She split them among Roger and 3 of his friends. Then Roger decided to give 2 of his cans to his brothers so that he now has 4 for himself. How many cans of silly string did Michelle have to start with?"""
    # Let x be the number of cans of silly string Michelle had to start with
    # Michelle split the cans among Roger and 3 friends, so each got x/4 cans
    # Roger received x/4 cans and gave 2 away, so he now has x/4 - 2 cans
    # Roger now has 4 cans, so x/4 - 2 = 4
    # Solving for x, we get x = 24

    # Therefore, Michelle had 24 cans of silly string to start with
    result = 24
    return result

print(solution())