def solution():
    # Calculate the number of votes that Mark receives in the first area
    mark_vote_area1 = 0.7 * 100000

    # Calculate the total number of voters in the remaining area
    total_voters_area2 = (100000 - mark_vote_area1) / 0.3

    # Calculate the number of votes that Mark receives in the remaining area
    mark_vote_area2 = 2 * mark_vote_area1

    # Calculate the total number of votes that Mark receives
    total_votes = mark_vote_area1 + mark_vote_area2

    result = total_votes
    return result

print(solution())