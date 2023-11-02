def solution():
    """The rim of a standard basketball hoop is 10 feet above the ground. Additionally, most experts will say that a player must be able to reach at least 6 inches above the rim to dunk a basketball. Suppose a basketball player is 6 feet tall and can reach 22 inches above their head using the wingspan of their arms. How high must this player be able to jump to reach 6 inches above the rim to dunk a basketball?"""
    hoop_height = 10 * 12 # convert 10 feet to inches
    player_height = 6 * 12 # convert 6 feet to inches
    required_reach = hoop_height + 6 # add 6 inches to the height of the hoop
    arm_span = 22 # inches
    total_reach = player_height + arm_span # total reach of the player
    required_jump_height = required_reach - total_reach # subtract the total reach from the required reach
    result = required_jump_height
    return result

print(solution())