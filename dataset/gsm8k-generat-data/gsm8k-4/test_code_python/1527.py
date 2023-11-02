def solution():
    """At the circus, the clown has 3 dozen balloons on a string in his hand. 3 boys and 12 girls buy a balloon each. How many balloons is the clown still holding?"""
    # Define the initial number of balloons
    initial_balloons = 3 * 12 # 3 dozen balloons = 36 balloons

    # Calculate the number of balloons sold
    balloons_sold = 3 + 12

    # Calculate the number of balloons the clown is still holding
    remaining_balloons = initial_balloons - balloons_sold

    # return the result
    result = remaining_balloons
    return result

print(solution())