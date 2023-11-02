def solution():
    # Find the number of votes Barry got
    votes_Barry = 2 * (3 + 8)  # Joey got 8 votes, and Barry got twice as many as 3 more than Joey's votes
    # Find the number of votes Marcy got
    votes_Marcy = 3 * votes_Barry  # Marcy got three times as many votes as Barry
    result = votes_Marcy
    return result

print(solution())