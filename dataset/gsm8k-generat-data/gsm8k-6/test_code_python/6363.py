def solution():
    # Calculate the height the player can reach
    height_reached = (6 * 12) + 22  # the player is 6 feet tall and can reach 22 inches above their head

    # Calculate the height the player needs to reach to dunk
    dunk_height = 10 + 6 + 6  # the rim of the basketball hoop is 10 feet high and the player must reach 6 inches above the rim to dunk

    # Calculate the height the player must be able to jump
    jump_height = dunk_height - height_reached

    result = jump_height
    return result

print(solution())