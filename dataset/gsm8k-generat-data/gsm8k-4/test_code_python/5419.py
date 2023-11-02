def solution():
    """In 2004, there were some kids at a cookout. In 2005, half the number of kids came to the cookout as compared to 2004. In 2006, 2/3 as many kids came to the cookout as in 2005. If there were 20 kids at the cookout in 2006, how many kids came to the cookout in 2004?"""
    # Let x be the number of kids at the cookout in 2004
    x = None

    # Calculate the number of kids at the cookout in 2005
    x_2005 = x / 2

    # Calculate the number of kids at the cookout in 2006
    x_2006 = 20

    # Calculate the number of kids at the cookout in 2005
    x_2005 = x_2006 / (2/3)

    # Calculate the number of kids at the cookout in 2004
    x = x_2005 * 2

    result = x
    return result

print(solution())