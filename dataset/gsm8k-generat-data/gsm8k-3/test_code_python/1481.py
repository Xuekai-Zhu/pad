def solution():
    """Mike watches TV for 4 hours every day.  On the days he plays video games he plays for half as long as he watches TV.  If he plays video games 3 days a week how long does he spend watching TV and playing video games?"""
    # Define the amount of time Mike watches TV each day
    TV_TIME = 4

    # Define the number of days Mike plays video games
    GAME_DAYS = 3

    # Calculate the total time Mike spends playing video games
    game_time = TV_TIME / 2 * GAME_DAYS

    # Calculate the total time Mike spends watching TV and playing video games
    total_time = game_time + TV_TIME * 7

    # Display the total time
    result = total_time
    return result

print(solution())