def solution():
    """At the circus, the clown has 3 dozen balloons on a string in his hand.  3 boys and 12 girls buy a balloon each.  How many balloons is the clown still holding?"""
    # Define the number of balloons the clown starts with
    START_BALLOONS = 3 * 12

    # Define the number of boys and girls who buy a balloon each
    boys = 3
    girls = 12

    # Calculate the total number of balloons sold
    balloons_sold = boys + girls

    # Calculate the number of balloons the clown is still holding
    balloons_left = START_BALLOONS - balloons_sold

    # Display the number of balloons the clown is still holding
    result = balloons_left
    return result

print(solution())