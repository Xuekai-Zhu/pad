def solution():
    """Brendan has entered a kickboxing competition and wins matches against multiple contestants. He wins all of the matches in the first 2 rounds, each of which had 6 matches, then wins half of the 4 matches in the last round. How many matches did Brendan win throughout the competition?"""
    round_one_matches = 6
    round_two_matches = 6
    round_three_matches = 4
    total_matches = (round_one_matches + round_two_matches) + (round_three_matches / 2)
    result = total_matches
    return result

print(solution())