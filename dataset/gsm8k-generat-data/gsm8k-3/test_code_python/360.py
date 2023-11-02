def solution():
    """Carl has a jar full of marbles. He takes out 12 marbles to play a game with, but he accidentally drops them and 1/2 the marbles get lost. So Carl takes out 10 more marbles. While he is playing his game his mother comes home with another bag of marbles for him, which has 25 marbles in it. If Carl can't find his lost marbles, then how many marbles is he going to put in the jar after he plays his game, from both his original marbles and the new ones?"""
    # Define the initial number of marbles, the number of lost marbles, and the number of marbles added by Carl's mother
    original_marbles = 0
    lost_marbles = 0
    added_marbles = 25

    # Calculate the number of marbles left after Carl drops 12 and loses half
    original_marbles -= 12
    lost_marbles = original_marbles / 2
    original_marbles -= lost_marbles

    # Add 10 more marbles
    original_marbles += 10

    # Calculate the total number of marbles
    total_marbles = original_marbles + added_marbles

    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())