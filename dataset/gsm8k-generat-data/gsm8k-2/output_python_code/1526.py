def solution():
    """At the circus, the clown has 3 dozen balloons on a string in his hand. 3 boys and 12 girls buy a balloon each. How many balloons is the clown still holding?"""
    balloons_per_dozen = 12
    total_balloons = 3 * balloons_per_dozen
    bought_balloons = 3 + 12
    remaining_balloons = total_balloons - bought_balloons
    result = remaining_balloons
    return result

print(solution())