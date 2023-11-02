def solution():
    # Calculate the total number of votes cast based on the given ratios
    unicorn_votes = 3 * 7  # 3 times as many people voted for the unicorn cake compared to the witch cake
    dragon_votes = 7 + 25  # the number of votes for the dragon cake was 25 more than the number of votes for the witch cake
    total_votes = unicorn_votes + dragon_votes + 7  # add up the votes for all three cakes, plus the initial 7 votes for the witch cake
    result = total_votes
    return result

print(solution())