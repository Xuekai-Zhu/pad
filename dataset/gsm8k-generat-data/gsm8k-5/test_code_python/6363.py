def solution():
    rim_height = 10  # The basketball rim is 10 feet above the ground
    dunk_height = rim_height + 0.5  # The player needs to reach 6 inches above the rim to dunk the ball
    player_height = 6  # The player is 6 feet tall
    reach = 22/12  # The player can reach 22 inches above their head using the wingspan of their arms

    # Calculate how high the player needs to jump to reach 6 inches above the rim
    jump_height = dunk_height - player_height - reach
    result = jump_height
    return result

print(solution())