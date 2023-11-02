def solution():
    witch_votes = 7  # 7 people voted for the witch cake
    unicorn_votes = 3 * witch_votes  # Unicorn cake received three times as many votes as the witch cake
    dragon_votes = witch_votes + 25  # Dragon cake received 25 more votes than the witch cake

    # Calculate the total number of votes cast
    total_votes = witch_votes + unicorn_votes + dragon_votes
    result = total_votes
    return result

print(solution())