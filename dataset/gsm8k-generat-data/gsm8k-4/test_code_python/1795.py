def solution():
    """Mary and her two friends came up with the idea of collecting marbles each day for their play on weekends. From Monday to Friday, Mary collected twice as many red marbles as Jenny and half the number of blue marbles collected by Anie, who collected 20 more red marbles than Mary and twice the number of blue marbles Jenny collected. If Jenny collected 30 red marbles and 25 blue marbles, what's the total number of blue marbles collected by the friends together?"""
    # Define the number of red and blue marbles collected by Jenny
    jenny_red = 30
    jenny_blue = 25

    # Define the number of red marbles collected by Mary
    mary_red = jenny_red * 2

    # Define the number of red and blue marbles collected by Anie
    anie_red = mary_red + 20
    anie_blue = jenny_blue * 2

    # Calculate the total number of blue marbles collected by the friends
    total_blue = jenny_blue + mary_red/2 + anie_blue

    # return the result
    result = total_blue
    return result

print(solution())