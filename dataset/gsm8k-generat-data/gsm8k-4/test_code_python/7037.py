def solution():
    """Fran is in charge of counting votes for the book club's next book, but she always cheats so her favorite gets picked. Originally, there were 10 votes for Game of Thrones, 12 votes for Twilight, and 20 votes for The Art of the Deal. Fran throws away 80% of the votes for The Art of the Deal and half the votes for Twilight. What percentage of the altered votes were for Game of Thrones?"""
    # Define the original vote counts
    got_votes = 10
    twilight_votes = 12
    art_votes = 20

    # Calculate the altered vote counts
    art_votes_altered = art_votes * 0.2
    twilight_votes_altered = twilight_votes * 0.5

    # Sum up the altered vote counts
    total_altered_votes = got_votes + twilight_votes_altered + art_votes_altered

    # Calculate the percentage of altered votes that were for Game of Thrones
    got_percentage = (got_votes / total_altered_votes) * 100

    result = round(got_percentage, 2)
    return result

print(solution())