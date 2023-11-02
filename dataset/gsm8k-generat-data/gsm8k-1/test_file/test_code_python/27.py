def solution():
    """Gunter is trying to count the jelly beans in a jar. He asks his friends how many they think are in the jar. One says 80. Another says 20 more than half the first one. A third says 25% more than the first one. What is their average guess?"""
    guess1 = 80
    guess2 = 20 + (0.5 * guess1)
    guess3 = 1.25 * guess1
    average_guess = (guess1 + guess2 + guess3) / 3
    result = average_guess
    return result

print(solution())