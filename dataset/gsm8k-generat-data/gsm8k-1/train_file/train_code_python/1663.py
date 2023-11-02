def solution():
    """Brendan has entered a kickboxing competition and wins matches against multiple contestants.
    He wins all of the matches in the first 2 rounds, each of which had 6 matches,
    then wins half of the 4 matches in the last round. How many matches did Brendan win throughout the competition?"""
    first_two_rounds = 2 * 6
    last_round = 4
    last_round_wins = last_round / 2
    total_matches_won = first_two_rounds + last_round_wins
    result = total_matches_won
    return result

print(solution())