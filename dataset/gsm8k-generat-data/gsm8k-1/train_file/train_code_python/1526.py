def solution():
    """At the circus, the clown has 3 dozen balloons on a string in his hand. 3 boys and 12 girls buy a balloon each. How many balloons is the clown still holding?"""
    balloons_per_dozen = 12
    initial_balloons = 3 * balloons_per_dozen
    balloons_bought = 3 + 12
    balloons_left = initial_balloons - balloons_bought
    result = balloons_left
    return result

print(solution())