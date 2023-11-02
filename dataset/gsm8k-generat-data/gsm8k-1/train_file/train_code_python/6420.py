def solution():
    """Allie, Rob, and Allyn each bought a bowl of grapes. Allie's bowl contained two more grapes than Rob's bowl. Allyn's bowl contained four more grapes than Allie's bowl. If Rob's bowl contained 25 grapes, what is the total combined number of grapes in all three bowls?"""
    robs_grapes = 25
    allies_grapes = robs_grapes + 2
    allyns_grapes = allies_grapes + 4
    total_grapes = robs_grapes + allies_grapes + allyns_grapes
    result = total_grapes
    return result

print(solution())