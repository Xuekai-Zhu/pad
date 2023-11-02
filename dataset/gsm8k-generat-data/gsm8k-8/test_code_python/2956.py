def solution():
    # Define the number of shots Cyrus made and attempted
    shots_attempted = 20
    shots_made = 0.8 * shots_attempted

    # Calculate the number of shots he missed
    shots_missed = shots_attempted - shots_made
    result = shots_missed
    return result

print(solution())