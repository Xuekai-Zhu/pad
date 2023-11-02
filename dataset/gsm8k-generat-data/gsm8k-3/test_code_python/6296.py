def solution():
    """A craftsman makes 16 jars. This is exactly twice the number of clay pots he made. 
    If each jar has 5 marbles and each clay pot has three times as many, how many marbles are there?"""
    
    # Find the number of clay pots made by the craftsman
    num_clay_pots = 16 // 2

    # Calculate the number of marbles in each clay pot
    marbles_per_pot = 3 * num_clay_pots

    # Calculate the total number of marbles
    total_marbles = (16 * 5) + (marbles_per_pot * num_clay_pots)

    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())