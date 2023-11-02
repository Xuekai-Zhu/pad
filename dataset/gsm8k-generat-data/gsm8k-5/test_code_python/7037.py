def solution():
    # Original vote counts
    got_votes = 10
    twilight_votes = 12
    art_of_deal_votes = 20

    # Discard votes
    art_of_deal_votes *= 0.2  # Discard 80% of Art of the Deal votes
    twilight_votes *= 0.5  # Discard half of Twilight votes

    # Total remaining altered votes
    total_votes = got_votes + twilight_votes + art_of_deal_votes

    # Calculate percentage of altered votes for Game of Thrones
    got_percentage = (got_votes / total_votes) * 100
    result = got_percentage
    return result

print(solution())