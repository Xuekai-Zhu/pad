def solution():
    """Fran is in charge of counting votes for the book club's next book, but she always cheats so her favorite gets picked. Originally, there were 10 votes for Game of Thrones, 12 votes for Twilight, and 20 votes for The Art of the Deal. Fran throws away 80% of the votes for The Art of the Deal and half the votes for Twilight. What percentage of the altered votes were for Game of Thrones?"""
    got_votes = 10
    twilight_votes = 12
    deal_votes = 20
    altered_deal_votes = deal_votes * 0.2
    altered_twilight_votes = twilight_votes * 0.5
    total_votes = got_votes + altered_twilight_votes + altered_deal_votes
    got_percentage = (got_votes / total_votes) * 100
    result = got_percentage
    
    return result

print(solution())