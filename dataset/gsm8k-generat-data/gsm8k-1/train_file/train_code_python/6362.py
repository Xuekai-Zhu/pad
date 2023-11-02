def solution():
    """The rim of a standard basketball hoop is 10 feet above the ground. Additionally, most experts will say that a player must be able to reach at least 6 inches above the rim to dunk a basketball. Suppose a basketball player is 6 feet tall and can reach 22 inches above their head using the wingspan of their arms. How high must this player be able to jump to reach 6 inches above the rim to dunk a basketball?"""
    rim_height = 10 * 12 # convert feet to inches
    reach_height = (6 * 12) + 22 # convert feet to inches and add arm reach
    player_height = 6 * 12 # convert feet to inches
    jump_height = reach_height - player_height - 6 # subtract 6 inches for dunking requirement
    result = jump_height / 12 # convert inches to feet
    return result

print(solution())