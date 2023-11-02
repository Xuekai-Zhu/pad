def solution():
    """Fran is in charge of counting votes for the book club's next book, but she always cheats so her favorite gets picked. Originally, there were 10 votes for Game of Thrones, 12 votes for Twilight, and 20 votes for The Art of the Deal. Fran throws away 80% of the votes for The Art of the Deal and half the votes for Twilight. What percentage of the altered votes were for Game of Thrones?"""
    # Define the original number of votes for each book
    got_votes = 10
    twilight_votes = 12
    art_votes = 20

    # Fran throws away 80% of the votes for The Art of the Deal
    art_votes = art_votes * 0.2

    # Fran throws away half the votes for Twilight
    twilight_votes = twilight_votes * 0.5

    # Calculate the total votes after Fran's tampering
    total_votes = got_votes + twilight_votes + art_votes

    # Calculate the percentage of votes for Game of Thrones
    got_percentage = (got_votes / total_votes) * 100

    # Display the percentage of votes for Game of Thrones
    result = got_percentage
    return result

print(solution())