def solution():
    """Albert has three times as many marbles as Angela. Angela has 8 more than Allison, who has 28 marbles. How many marbles do Albert and Allison have?"""
    allison_marbles = 28
    angela_marbles = allison_marbles + 8
    albert_marbles = angela_marbles * 3
    total_marbles = allison_marbles + albert_marbles
    result = total_marbles
    return result

print(solution())