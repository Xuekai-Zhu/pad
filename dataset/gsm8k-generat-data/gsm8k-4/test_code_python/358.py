def solution():
    """Carl has a jar full of marbles. He takes out 12 marbles to play a game with, but he accidentally drops them and 1/2 the marbles get lost. So Carl takes out 10 more marbles. While he is playing his game his mother comes home with another bag of marbles for him, which has 25 marbles in it. If Carl can't find his lost marbles, then how many marbles is he going to put in the jar after he plays his game, from both his original marbles and the new ones?"""
    # Define the initial number of marbles
    initial_marbles = None

    # Calculate the number of marbles left after dropping and losing half of them
    marbles_left = (initial_marbles - 12) / 2

    # Calculate the total number of marbles after taking out 10 more and adding the new bag of marbles
    total_marbles = marbles_left + 10 + 25

    # return the result
    result = total_marbles
    return result

print(solution())