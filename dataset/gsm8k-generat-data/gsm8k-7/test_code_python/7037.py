def solution():
    got_votes = 10
    twilight_votes = 12
    deal_votes = 20
    fran_discount = 0.8
    twilight_discount = 0.5

    # Calculate the number of votes for The Art of the Deal after Fran's discount
    deal_votes_discounted = deal_votes * fran_discount

    # Calculate the number of votes for Twilight after Fran's discount
    twilight_votes_discounted = twilight_votes * twilight_discount

    # Calculate the total number of altered votes
    total_altered_votes = got_votes + twilight_votes_discounted + deal_votes_discounted

    # Calculate the percentage of altered votes that were for Game of Thrones
    got_percentage = (got_votes / total_altered_votes) * 100
    result = got_percentage
    return result

print(solution())