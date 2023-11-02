def solution():
    """Carl has a jar full of marbles. He takes out 12 marbles to play a game with, but he accidentally drops them and 1/2 the marbles get lost. So Carl takes out 10 more marbles. While he is playing his game his mother comes home with another bag of marbles for him, which has 25 marbles in it. If Carl can't find his lost marbles, then how many marbles is he going to put in the jar after he plays his game, from both his original marbles and the new ones?"""
    initial_marbles = 0
    marbles_played = 12
    marbles_lost = marbles_played / 2
    marbles_taken_out = 10
    new_marbles = 25
    marbles_remaining = initial_marbles - marbles_lost + marbles_taken_out + new_marbles
    result = marbles_remaining
    return result

print(solution())