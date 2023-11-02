def solution():
    """At a softball game, three players are having a sunflower eating contest. The first player eats 78 seeds. The second eats 53 seeds. The third eats 30 more seeds than the second. How many do they eat in total?"""
    # Define the number of seeds each player eats
    player1 = 78
    player2 = 53
    player3 = player2 + 30 # player 3 eats 30 more seeds than player 2

    # Calculate the total number of seeds eaten
    total_seeds = player1 + player2 + player3

    # Display the total number of seeds eaten
    result = total_seeds
    return result

print(solution())