def solution():
    total_votes = 10 + 12 + 20
    game_of_thrones_votes = 10
    twilight_votes = 12
    art_of_the_deal_votes = 20
    art_of_the_deal_votes_after_fraud = art_of_the_deal_votes * 0.2
    twilight_votes_after_fraud = twilight_votes * 0.5
    total_votes_after_fraud = game_of_thrones_votes + twilight_votes_after_fraud + art_of_the_deal_votes_after_fraud
    game_of_thrones_percentage = (game_of_thrones_votes / total_votes_after_fraud) * 100
    result = game_of_thrones_percentage
    return result

print(solution())