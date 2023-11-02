def solution():
    # Define the length of the match in minutes
    match_length = 2 * 60

    # Calculate the number of 15-minute intervals in the match
    intervals_in_match = match_length / 15

    # Calculate the total number of goals Xavier can score in the match
    total_goals = intervals_in_match * 2

    # Calculate Xavier's average number of goals per match
    average_goals = total_goals / (match_length / 60)
    result = average_goals
    return result

print(solution())