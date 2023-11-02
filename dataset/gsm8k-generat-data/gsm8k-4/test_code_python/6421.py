def solution():
    """Allie, Rob, and Allyn each bought a bowl of grapes. Allie's bowl contained two more grapes than Rob's bowl. Allyn's bowl contained four more grapes than Allie's bowl. If Rob's bowl contained 25 grapes, what is the total combined number of grapes in all three bowls?"""
    # Define the number of grapes in Rob's bowl
    rob_grapes = 25

    # Calculate the number of grapes in Allie's bowl
    allie_grapes = rob_grapes + 2

    # Calculate the number of grapes in Allyn's bowl
    allyn_grapes = allie_grapes + 4

    # Calculate the total number of grapes in all three bowls
    total_grapes = rob_grapes + allie_grapes + allyn_grapes

    # return the result
    result = total_grapes
    return result

print(solution())