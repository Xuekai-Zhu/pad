def solution():
    # Calculate the total number of original votes
    total_votes = 10 + 12 + 20  

    # Calculate the number of votes after Fran cheats
    altered_votes = (0.2 * 20) + (0.5 * 12) + 10  # Fran throws away 80% of The Art of the Deal votes and half of the Twilight votes, and adds 10 fraudulent votes for her favorite

    # Calculate the percentage of altered votes for Game of Thrones
    got_votes = 10  # votes for Game of Thrones remain unchanged
    percentage_votes = (got_votes / altered_votes) * 100
    result = percentage_votes
    return result

print(solution())