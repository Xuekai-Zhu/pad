def solution():
    """John plays a game for 4 hours a day every day for 2 weeks.  After all that time, he is only 40% done.  He increased his playtime to 7 hours a day.  How long until he finishes the game?"""
    # Calculate total hours played in first 2 weeks
    hours_played = 4 * 7 * 2

    # Calculate percentage of game completed in first 2 weeks
    progress = 0.4

    # Calculate total hours needed to complete the game
    total_hours = hours_played / progress

    # Calculate remaining hours needed to complete the game
    remaining_hours = total_hours - hours_played

    # Calculate number of days needed to complete the game with increased playtime
    days_needed = remaining_hours / (7 - 4)

    # Display the number of days needed
    result = days_needed
    return result

print(solution())