def solution():
    total_spectators = 10000  # Total number of spectators at the match
    men = 7000  # Number of male spectators
    women = total_spectators - men  # Number of female spectators
    children = 5 * women  # Number of child spectators is 5 times as many as women
    result = children
    return result

print(solution())