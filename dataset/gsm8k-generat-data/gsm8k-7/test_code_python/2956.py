def solution():
    total_shots_attempted = 20
    percentage_made = 0.8

    # Calculate the number of shots Cyrus made
    shots_made = total_shots_attempted * percentage_made

    # Calculate the number of shots he missed
    shots_missed = total_shots_attempted - shots_made
    result = shots_missed
    return result

print(solution())