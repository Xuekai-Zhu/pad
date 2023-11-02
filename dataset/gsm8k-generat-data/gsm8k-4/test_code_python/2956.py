def solution():
    """In a basketball game, Cyrus made exactly eighty percent of the shots he attempted. He attempted twenty shots. How many times did he miss the shots?"""
    # Define the number of shots attempted and the percentage of shots made
    shots_attempted = 20
    shots_made_percentage = 80

    # Calculate the number of shots made
    shots_made = (shots_made_percentage / 100) * shots_attempted

    # Calculate the number of shots missed
    shots_missed = shots_attempted - shots_made

    # Return the number of shots missed
    result = shots_missed
    return result

print(solution())