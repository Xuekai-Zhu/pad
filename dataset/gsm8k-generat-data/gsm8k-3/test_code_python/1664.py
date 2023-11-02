def solution():
    """Brendan has entered a kickboxing competition and wins matches against multiple contestants. He wins all of the matches in the first 2 rounds, each of which had 6 matches, then wins half of the 4 matches in the last round. How many matches did Brendan win throughout the competition?"""
    # Define the number of matches in the first two rounds and the last round
    round1_matches = 6
    round2_matches = 6
    round3_matches = 4

    # Calculate the total number of matches Brendan won
    total_matches_won = round1_matches + round2_matches + (round3_matches/2)

    # Display the total number of matches won
    result = total_matches_won
    return result

print(solution())