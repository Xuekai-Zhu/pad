def solution():
    """In 2004, there were some kids at a cookout. In 2005, half the number of kids came to the cookout as compared to 2004. In 2006, 2/3 as many kids came to the cookout as in 2005. If there were 20 kids at the cookout in 2006, how many kids came to the cookout in 2004?"""
    # Let x be the number of kids in 2004
    # In 2005, half the number of kids came to the cookout, so there were x/2 kids
    # In 2006, 2/3 as many kids came to the cookout as in 2005, so there were (2/3)(x/2) = x/3 kids
    # Since there were 20 kids in 2006, we have x/3 = 20
    # Solving for x, we get x = 60

    # Therefore, there were 60 kids at the cookout in 2004
    result = 60
    return result

print(solution())