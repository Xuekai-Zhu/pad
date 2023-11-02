def solution():
    """Patricia is making a highlight film about her basketball team. She recorded video of every player and plans to put it all together in a longer movie. She has 130 seconds of the point guard, 145 seconds of the shooting guard, 85 seconds of the small forward, 60 seconds of the power forward, and 180 seconds of the center. How on average, how many minutes does each player get?"""
    # Define the number of seconds for each player
    PG_SECONDS = 130
    SG_SECONDS = 145
    SF_SECONDS = 85
    PF_SECONDS = 60
    C_SECONDS = 180

    # Calculate the total number of seconds for all the players
    total_seconds = PG_SECONDS + SG_SECONDS + SF_SECONDS + PF_SECONDS + C_SECONDS

    # Convert total seconds to minutes
    total_minutes = total_seconds / 60

    # Calculate the average number of minutes each player gets
    num_players = 5
    avg_minutes = total_minutes / num_players

    # Display the average number of minutes each player gets
    result = avg_minutes
    return result

print(solution())