def solution():
    """In a basketball game, Cyrus made exactly eighty percent of the shots he attempted. He attempted twenty shots. How many times did he miss the shots?"""
    # Define the percentage of shots made by Cyrus
    SHOTS_MADE_PERCENTAGE = 80

    # Define the number of shots attempted by Cyrus
    shots_attempted = 20

    # Calculate the number of shots made by Cyrus
    shots_made = (SHOTS_MADE_PERCENTAGE / 100) * shots_attempted

    # Calculate the number of shots missed by Cyrus
    shots_missed = shots_attempted - shots_made

    # Display the number of shots missed
    result = shots_missed
    return result

print(solution())