def solution():
    """Allie, Rob, and Allyn each bought a bowl of grapes. Allie's bowl contained two more grapes than Rob's bowl. Allyn's bowl contained four more grapes than Allie's bowl. If Rob's bowl contained 25 grapes, what is the total combined number of grapes in all three bowls?"""
    rob_grapes = 25
    allie_grapes = rob_grapes + 2
    allyn_grapes = allie_grapes + 4
    total_grapes = rob_grapes + allie_grapes + allyn_grapes
    result = total_grapes
    return result

print(solution())