def solution():
    """Carl has a jar full of marbles. He takes out 12 marbles to play a game with, but he accidentally drops them and 1/2 the marbles get lost. So Carl takes out 10 more marbles. While he is playing his game his mother comes home with another bag of marbles for him, which has 25 marbles in it. If Carl can't find his lost marbles, then how many marbles is he going to put in the jar after he plays his game, from both his original marbles and the new ones?"""
    original_marbles = 0
    new_marbles = 25
    lost_marbles = 6
    played_marbles = 12 + 10
    remaining_marbles = original_marbles - lost_marbles + played_marbles + new_marbles
    result = remaining_marbles
    return result

print(solution())