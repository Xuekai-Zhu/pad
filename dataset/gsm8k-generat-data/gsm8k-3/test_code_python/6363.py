def solution():
    """The rim of a standard basketball hoop is 10 feet above the ground.  Additionally, 
    most experts will say that a player must be able to reach at least 6 inches above the 
    rim to dunk a basketball.  Suppose a basketball player is 6 feet tall and can reach 
    22 inches above their head using the wingspan of their arms.  How high must this player 
    be able to jump to reach 6 inches above the rim to dunk a basketball?"""
    # Define the height of the basketball hoop and the minimum height required to dunk
    HOOP_HEIGHT = 10 # feet
    MIN_HEIGHT = 6/12 # feet

    # Convert the player's height and reach to feet
    player_height = 6 # feet
    reach = 22/12 # feet

    # Calculate the maximum height the player can reach on their tiptoes
    max_reach = player_height + reach

    # Calculate the jumping height required to reach the minimum dunking height
    jump_height = MIN_HEIGHT - (HOOP_HEIGHT - max_reach)

    # Display the jumping height required
    result = jump_height
    return result

print(solution())