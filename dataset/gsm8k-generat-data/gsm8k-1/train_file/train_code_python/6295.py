def solution():
    """A craftsman makes 16 jars. This is exactly twice the number of clay pots he made. If each jar has 5 marbles and each clay pot has three times as many, how many marbles are there?"""
    jars = 16
    clay_pots = jars / 2
    marbles_per_jar = 5
    marbles_per_pot = marbles_per_jar * 3
    total_marbles = (jars * marbles_per_jar) + (clay_pots * marbles_per_pot)
    result = total_marbles
    
    return result

print(solution())