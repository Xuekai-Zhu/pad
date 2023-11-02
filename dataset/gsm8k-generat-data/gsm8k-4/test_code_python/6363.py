def solution():
    """The rim of a standard basketball hoop is 10 feet above the ground. Additionally, most experts will say that a player must be able to reach at least 6 inches above the rim to dunk a basketball. Suppose a basketball player is 6 feet tall and can reach 22 inches above their head using the wingspan of their arms. How high must this player be able to jump to reach 6 inches above the rim to dunk a basketball?"""

    # Define the height of the basketball rim and the additional height required to dunk
    rim_height = 10  # feet
    dunk_addition = 0.5  # feet

    # Define the height of the player and their reach above their head
    player_height = 6  # feet
    player_reach = 1.83  # feet (22 inches = 1.83 feet)

    # Calculate the player's total standing reach (height + reach)
    player_reach_total = player_height + player_reach

    # Calculate the minimum jumping height required to reach 6 inches above the rim
    jumping_height = rim_height - player_reach_total - dunk_addition

    result = jumping_height
    return result

print(solution())