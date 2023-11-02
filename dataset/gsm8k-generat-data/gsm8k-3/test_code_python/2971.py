def solution():
    """Flies are Betty's frog's favorite food. Every day the frog eats 2 flies. Betty puts the flies she finds in a bottle. In the morning Betty catches 5 flies inside a bottle, and in the afternoon she catches 6 more, but when she removes the lid, one escapes. Betty wants to gather the whole week's food for her frog. How many more flies does she need?"""
    # Define the number of flies Betty catches in the morning and afternoon
    MORNING_FLIES = 5
    AFTERNOON_FLIES = 6

    # Calculate the number of flies she catches per day
    daily_flies = MORNING_FLIES + AFTERNOON_FLIES - 1

    # Calculate the number of flies she needs for a week
    weekly_flies = 7 * 2

    # Calculate the number of flies she still needs to catch
    remaining_flies = weekly_flies - (daily_flies * 7)

    # Display the number of flies she still needs to catch
    result = remaining_flies
    return result

print(solution())