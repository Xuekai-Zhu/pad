def solution():
    """There were 10000 spectators at a basketball match. 7000 of them were men. Of the remaining spectators, there were 5 times as many children as women. How many children were there?"""
    total_spectators = 10000
    men = 7000
    women = total_spectators - men
    children = 5 * women
    result = children
    return result

print(solution())