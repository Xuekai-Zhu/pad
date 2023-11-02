def solution():
    # Define original vote counts
    got_votes = 10
    twilight_votes = 12
    art_of_deal_votes = 20

    # Throw away 80% of Art of the Deal votes
    art_of_deal_votes *= 0.2

    # Throw away half of Twilight votes
    twilight_votes *= 0.5

    # Calculate total altered votes
    total_altered_votes = got_votes + twilight_votes + art_of_deal_votes

    # Calculate percentage of altered votes for Game of Thrones
    got_altered_percentage = (got_votes / total_altered_votes) * 100
    result = got_altered_percentage
    return result

print(solution())