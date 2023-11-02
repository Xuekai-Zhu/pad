def solution():
    """Marcy's grade is electing their class president. Marcy got three times as many votes as Barry, who got twice as many as 3 more than the number of votes Joey got. If Joey got 8 votes, how many votes did Marcy get?"""
    # Define the number of votes Joey got
    joey_votes = 8

    # Calculate the number of votes Barry got
    barry_votes = (joey_votes + 3) * 2

    # Calculate the number of votes Marcy got
    marcy_votes = barry_votes * 3

    # Display the number of votes Marcy got
    result = marcy_votes
    return result

print(solution())