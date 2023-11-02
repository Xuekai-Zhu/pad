def solution():
    party_nickname = "Grand Old Party"
    election_year = 1980
    winner_party = "Republican"
    if winner_party == "Republican" and party_nickname in winner_party:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())