def solution():
    
    got_votes = 10
    twilight_votes = 12
    art_of_deal_votes = 20
    altered_art_of_deal_votes = art_of_deal_votes * 0.2
    altered_twilight_votes = twilight_votes * 0.5
    total_votes = got_votes + altered_twilight_votes + altered_art_of_deal_votes
    percentage = (got_votes / total_votes) * 100
    result = percentage
    return result

print(solution())