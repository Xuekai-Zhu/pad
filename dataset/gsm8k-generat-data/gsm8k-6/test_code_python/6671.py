def solution():
    # Calculate the number of women and men at the party
    women = 100 * 0.5
    men = 100 * 0.35
    
    # Calculate the number of children at the party
    children = 100 - women - men
    result = children
    return result

print(solution())