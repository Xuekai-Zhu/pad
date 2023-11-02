def solution():
    """John plays a game for 4 hours a day every day for 2 weeks. After all that time, he is only 40% done. He increased his playtime to 7 hours a day. How long until he finishes the game?"""
    # Define the total playtime required to finish the game
    total_playtime = 100

    # Define the initial playtime and completion percentage
    initial_playtime = 4 * 14
    initial_completion = 40

    # Calculate the remaining playtime and completion percentage
    remaining_playtime = total_playtime - initial_completion * initial_playtime / 100
    remaining_completion = 100 - initial_completion

    # Calculate the number of days required to finish the game
    days_required = remaining_playtime / (7 * remaining_completion / 100)

    # Return the result
    result = days_required
    return result

print(solution())