def solution():
    """At a softball game, three players are having a sunflower eating contest. The first player eats 78 seeds. The second eats 53 seeds. The third eats 30 more seeds than the second. How many do they eat in total?"""
    # Define the number of seeds eaten by each player
    player1_seeds = 78
    player2_seeds = 53
    player3_seeds = player2_seeds + 30

    # Calculate the total number of seeds eaten
    total_seeds = player1_seeds + player2_seeds + player3_seeds

    # Return the result
    result = total_seeds
    return result

print(solution())